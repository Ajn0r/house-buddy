from django.shortcuts import render, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Categories, Entries
from .forms import NewCategoryForm



class CategoryList(generic.ListView):
    model = Categories
    queryset = Categories.objects.order_by('name')
    template_name = 'category_page.html'
    paginate_by = 6


class NewCategory(generic.CreateView):
    model = Categories
    fields = ['name']
    template_name = 'new_category.html'
    # form_class = NewCategoryForm
    success_url = 'categories'


class EditCategory(generic.UpdateView):
    model = Categories
    fields = ['name']
    template_name = 'edit_category.html'
    success_url = '/categories'


class DeleteCategory(generic.DeleteView):
    model = Categories
    template_name = 'category_page.html'
    success_url = '/categories'


class EntryList(generic.ListView):
    model = Entries
    queryset = Entries.objects.order_by('category')
    template_name = 'entries_page.html'
    paginate_by = 6


class NewEntry(generic.CreateView):
    model = Entries
    fields = ['title', 'category', 'amount', 'date_of_purchase', 'description']
    template_name = 'new_entry.html'
    success_url = 'entries'

