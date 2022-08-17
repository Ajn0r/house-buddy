from django.shortcuts import render, reverse, get_object_or_404, redirect, HttpResponseRedirect
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
# from django.urls import reverse_lazy
from django.db import IntegrityError
from .models import Categories, Entries
from .forms import NewCategoryForm, NewEntryForm


class CategoryDetails(LoginRequiredMixin, DetailView):
    model = Categories
    template_name = 'category_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetails, self).get_context_data()
        list_obj = self.object
        context['object'] = list_obj
        context['items'] = Entries.objects.filter(category=list_obj)
        return context


class CategoryList(LoginRequiredMixin, ListView):
    model = Categories
    queryset = Categories.objects.order_by('name')
    template_name = 'category_page.html'
    paginate_by = 6

    def get_queryset(self):
        user = self.request.user
        return Categories.objects.filter(user=user)


class NewCategory(LoginRequiredMixin, CreateView):
    model = Categories
    template_name = 'new_category.html'
    fields = ['name']
    # form_class = NewCategoryForm
    success_url = '/categories'

    def form_valid(self, form):
        try:
            form.instance.user = self.request.user
            return super().form_valid(form)
        except IntegrityError:
            messages.error(self.request, 'This category already exists')
            return redirect('new_category')


class EditCategory(LoginRequiredMixin, UpdateView):
    model = Categories
    fields = ['name']
    template_name = 'edit_category.html'
    success_url = '/categories'


class DeleteCategory(LoginRequiredMixin, DeleteView):
    model = Categories
    success_url = '/categories'
    template_name = 'categories_confirm_delete.html'


class EntryList(LoginRequiredMixin, ListView):
    model = Entries
    queryset = Entries.objects.order_by('category')
    template_name = 'entries_page.html'
    paginate_by = 6

    def get_queryset(self):
        user = self.request.user
        return Entries.objects.filter(user=user)


class NewEntry(LoginRequiredMixin, CreateView):
    model = Entries
    form_class = NewEntryForm
    # fields = ['title', 'category', 'amount', 'image','date_of_purchase', 'description']
    template_name = 'new_entry.html'
    success_url = 'entries'

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""
        kwargs = super(NewEntry, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EntryDetail(LoginRequiredMixin, DetailView):
    model = Entries
    template_name = 'entry_detail.html'


class EditEntry(LoginRequiredMixin, UpdateView):
    model = Entries
    fields = ['title', 'category', 'amount', 'date_of_purchase', 'description']
    template_name = 'edit_entry.html'
    success_url = '/entries'


class DeleteEntry(LoginRequiredMixin, DeleteView):
    model = Entries
    template_name = 'entries_page.html'
    success_url = '/entries'


class MyPage(LoginRequiredMixin, TemplateView):
    model = Categories
    template_name = 'mypage.html'

    def get_context_data(self, **kwargs):
        """
        To be able to reach both Category and Entries
        returns only the users objects.
        """
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['categories'] = Categories.objects.filter(user=user)
        context['entries'] = Entries.objects.filter(user=user)
        return context
