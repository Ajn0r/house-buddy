from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, View
from .models import Blogpost, Comments
from .forms import CommentForm


class BlogList(ListView):
    """
    View to display blogposts on blogpage
    """
    model = Blogpost
    template_name = 'blog.html'
    paginate_by = 2
    queryset = Blogpost.objects.filter(process=1).order_by('-created_on')


class BlogDetail(View):
    """
    A view to display the blogposts full details
    This code is greatly inspired by the code institue
    walkthrouh 'I think therefore I blog
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Blogpost.objects.filter(process=1)
        blogpost = get_object_or_404(queryset, slug=slug)
        comments = blogpost.comments.filter(approved=True).order_by('posted_on')
        liked = False
        if blogpost.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request, 
            'blogpost_detail.html',
            {
                'blogpost': blogpost,
                'comments': comments,
                'commented': False,
                'liked': False,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Blogpost.objects.filter(process=1)
        blogpost = get_object_or_404(queryset, slug=slug)
        comments = blogpost.comments.filter(approved=True).order_by('created_on')
        liked = False
        if blogpost.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.blogpost = blogpost
            comment.save

        return render(
            request, 
            'blogpost_detail.html',
            {
                'blogpost': blogpost,
                'comments': comments,
                'commented': False,
                'liked': False,
                'comment_form': CommentForm()
            },
        )
