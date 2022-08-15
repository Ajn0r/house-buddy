from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Categories, Entries


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
    fields = ['user', 'name']
    template_name = 'new_category.html'
    # form_class = NewCategoryForm
    success_url = '/categories'


class EditCategory(LoginRequiredMixin, UpdateView):
    model = Categories
    fields = ['name']
    template_name = 'edit_category.html'
    success_url = '/categories'


class DeleteCategory(LoginRequiredMixin, DeleteView):
    model = Categories
    template_name = 'category_page.html'
    success_url = '/categories'


class EntryList(LoginRequiredMixin, ListView):
    model = Entries
    queryset = Entries.objects.order_by('category')
    template_name = 'entries_page.html'
    paginate_by = 6


class NewEntry(LoginRequiredMixin, CreateView):
    model = Entries
    fields = ['title', 'category', 'amount', 'date_of_purchase', 'description']
    template_name = 'new_entry.html'
    success_url = 'entries'


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
