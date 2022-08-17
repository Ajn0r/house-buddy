from django.shortcuts import render, reverse, get_object_or_404, redirect, HttpResponseRedirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.db import IntegrityError
from .models import Categories, Entries
from .forms import NewEntryForm


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


class CategoryDetails(LoginRequiredMixin, DetailView):
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


class NewCategory(LoginRequiredMixin, CreateView):
    """
    A view to create new categories
    """
    model = Categories
    template_name = 'new_category.html'
    fields = ['name']
    success_url = reverse_lazy('categories')

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
            messages.error(self.request, 'This category already exists')
            return redirect('new_category')


class EditCategory(LoginRequiredMixin, UpdateView):
    """
    A view to update categories
    """
    model = Categories
    fields = ['name']
    template_name = 'edit_category.html'
    success_url = reverse_lazy('categories')


class DeleteCategory(LoginRequiredMixin, DeleteView):
    """
    A view to delete categories
    """
    model = Categories
    success_url = reverse_lazy('categories')
    template_name = 'categories_confirm_delete.html'


class EntryList(LoginRequiredMixin, ListView):
    """
    A view to display all entries
    """
    model = Entries
    queryset = Entries.objects.order_by('category')
    template_name = 'entries_page.html'
    paginate_by = 6

    def get_queryset(self):
        """
        A function to only display entries connected to the user
        """
        user = self.request.user
        return Entries.objects.filter(user=user)


class EntryDetail(LoginRequiredMixin, DetailView):
    """
    A view to show the details of a entry
    """
    model = Entries
    template_name = 'entry_detail.html'


class NewEntry(LoginRequiredMixin, CreateView):
    """
    A view for creating new entries
    """
    model = Entries
    form_class = NewEntryForm
    template_name = 'new_entry.html'
    success_url = reverse_lazy('entries')

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


class EditEntry(LoginRequiredMixin, UpdateView):
    """
    A veiw to update entries
    """
    model = Entries
    fields = ['title', 'category', 'amount', 'date_of_purchase', 'description']
    template_name = 'edit_entry.html'
    success_url = reverse_lazy('entries')


class DeleteEntry(LoginRequiredMixin, DeleteView):
    """
    A view to delete entries, this is done via a modal
    in the detailview, so no confirm delete page needed.
    """
    model = Entries
    template_name = 'entries_page.html'
    success_url = reverse_lazy('entries')


class MyPage(LoginRequiredMixin, TemplateView):
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
        context['entries'] = Entries.objects.filter(user=user)
        return context
