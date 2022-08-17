from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blogpost, Comments


class BlogList(ListView):
    """
    View to display blogposts on blogpage
    """
    model = Blogpost
    template_name = 'blog.html'
    paginate_by = 2
    ordering = '-created_on'


class BlogDetail(DetailView):
    """
    A view to display the blogposts full details
    """
    model = Blogpost
    template_name = 'blogpost_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_detail = self.object
        context['object'] = post_detail
        context['blogpost'] = Blogpost.objects.filter(title=post_detail)
        return context
