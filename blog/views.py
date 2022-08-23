from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from django.views.generic import ListView, View
from django.core.paginator import Paginator
from .models import Blogpost, Comments
from .forms import CommentForm


class BlogList(ListView):
    """
    View to display blogposts on blogpage
    """
    model = Blogpost
    template_name = 'blog.html'
    paginate_by = 4
    queryset = Blogpost.objects.filter(process=1).order_by('-created_on')

class BlogDetail(View):
    """
    A view to display the blogposts full details
    This code is greatly inspired by the code institue
    walkthrouh 'I think therefore I blog
    """
    def get(self, request, slug, *args, **kwargs):

        queryset = Blogpost.objects.filter(process=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('posted_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request, 
            'blogpost_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Blogpost.objects.filter(process=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('posted_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = self.request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

        return render(
            request, 
            'blogpost_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'comment_form': CommentForm(),
                'liked': liked,
            },
        )


class LikePost(View):

    def post(self, request, slug):
        post = get_object_or_404(Blogpost, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('blogpost', args=[slug]))
