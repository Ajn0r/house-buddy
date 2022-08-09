from django.shortcuts import render, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
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