from django.shortcuts import render
from django.views import generic
from .models import Categories, Entries


class CategoryList(generic.ListView):
    model = Categories
    queryset = Categories.objects.order_by('name')
    template_name = 'category_page.html'
    paginate_by = 6

