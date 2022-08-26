from django.shortcuts import reverse, redirect
from django.views.generic import (
    DetailView, ListView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.db import IntegrityError
from django_filters.views import FilterView
from .models import Categories, Entries
from .forms import NewEntryForm, NewCategoryForm
from .filters import EntryFilter


class CategoryList(LoginRequiredMixin, ListView):
    """
    A view to display a list of all the categories
    """
    model = Categories
    queryset = Categories.objects.order_by('name')
    template_name = 'category_page.html'
    paginate_by = 6

    def get_queryset(self):
        """
        Gets only the categories that the user has made
        """
        user = self.request.user
        return Categories.objects.filter(user=user)


class CategoryDetails(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    A view to dislay the details of the category, in this instance its
    all the entries connected to the category the user chooses to display.
    """
    model = Categories
    template_name = 'category_detail.html'
    success_url = reverse_lazy('categories')

    def get_context_data(self, **kwargs):
        """
        Function to display all the objects in the specific category
        This code is inspired by a solution on stackoverflow by 'Adil Mohak'
        """
        context = super(CategoryDetails, self).get_context_data()
        category_obj = self.object
        context['object'] = category_obj
        context['items'] = Entries.objects.filter(category=category_obj)
        return context

    def test_func(self):
        """
        function to make sure that the user cannot
        reach another users categories
        """
        category = self.get_object()
        return category.user == self.request.user


class NewCategory(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    A view to create new categories
    """
    model = Categories
    template_name = 'new_category.html'
    form_class = NewCategoryForm
    success_url = reverse_lazy('categories')
    success_message = 'Category was created successfully'

    def form_valid(self, form):
        """
        Function to validate form, catches IntegrityErrors,
        such as if a user tries to add a category with the same name
        that already exists.
        """
        try:
            form.instance.user = self.request.user
            return super().form_valid(form)
        except IntegrityError:
            name = form.instance.name
            messages.error(
                self.request,
                f"You already have a category called: {name}."
                " Try something else or go "
                "<a href='%s'>back</a> to categories" % reverse('categories')
                )
            return redirect('new_category')


class EditCategory(
    LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView
):
    """
    A view to update categories
    """
    model = Categories
    fields = ['name']
    template_name = 'edit_category.html'
    success_url = reverse_lazy('categories')
    success_message = 'Your category was updated successfully'

    def test_func(self):
        """
        function to make sure that the user cannot
        edit another users category
        """
        category = self.get_object()
        return category.user == self.request.user


class DeleteCategory(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    A view to delete categories
    """
    model = Categories
    template_name = 'categories_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, 'Category successfully deleted')
        return reverse_lazy('categories')

    def test_func(self):
        """
        function to make sure that the user cannot
        delete another users category
        """
        category = self.get_object()
        return category.user == self.request.user


class EntryList(LoginRequiredMixin, FilterView):
    """
    A view to display all entries
    """
    model = Entries
    queryset = Entries.objects.order_by('category')
    template_name = 'entries_page.html'
    paginate_by = 6
    filterset_class = EntryFilter

    def get_queryset(self):
        """
        A function to only display entries connected to the user
        """
        user = self.request.user
        return Entries.objects.filter(user=user)


class EntryDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    A view to show the details of a entry
    """
    model = Entries
    template_name = 'entry_detail.html'

    def test_func(self):
        """
        function to make sure that the user cannot
        reach another users entries
        """
        entry = self.get_object()
        return entry.user == self.request.user


class NewEntry(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    A view for creating new entries
    """
    model = Entries
    form_class = NewEntryForm
    template_name = 'new_entry.html'
    success_url = reverse_lazy('entries')
    success_message = 'Entry succesfully created'

    def get_form_kwargs(self):
        """
        Passes the request object to the form class, so that the
        user can only chose from their own categories.
        This code is greatly inspired by a post by
        Alice Campkin on medium.com/analytics-vidhya
        """
        kwargs = super(NewEntry, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        """
        Validates the form and makes sure its connected to
        the user.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditEntry(
    LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView
):
    """
    A veiw to update entries
    """
    model = Entries
    form_class = NewEntryForm
    template_name = 'edit_entry.html'
    success_url = reverse_lazy('entries')
    success_message = 'Entry successfully updated'

    def get_form_kwargs(self):
        """
        Passes the request object to the form class, so that the
        user can only chose from their own categories.
        This code is greatly inspired by a post by
        Alice Campkin on medium.com/analytics-vidhya
        """
        kwargs = super(EditEntry, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def test_func(self):
        """
        function to make sure that the user cannot
        edit another users entry
        """
        entry = self.get_object()
        return entry.user == self.request.user


class DeleteEntry(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    A view to delete entries, this is done via a modal
    in the detailview, so no confirm delete page needed.
    """
    model = Entries
    template_name = 'entries_page.html'

    def get_success_url(self):
        messages.success(self.request, 'Entry successfully deleted')
        return reverse_lazy('entries')

    def test_func(self):
        """
        function to make sure that the user cannot
        delete another users entry
        """
        entry = self.get_object()
        return entry.user == self.request.user


class MyPage(LoginRequiredMixin, ListView):
    """
    A view for the 'My Page'
    """
    model = Categories
    template_name = 'mypage.html'

    def get_context_data(self, **kwargs):
        """
        To be able to reach both Category and Entries,
        returns only the users objects.
        """
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.filter(user=user)
        context['entries'] = Entries.objects.filter(user=user).order_by(
            '-date_added')
        return context
