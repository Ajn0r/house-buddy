from django.shortcuts import render
from django.views.generic import ListView
from .models import Blogpost, Comments


class BlogList(ListView):
    model = Blogpost
    template_name = 'blog.html'

