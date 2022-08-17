from . models import Comments, Blogpost
from django.forms import ModelForm


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['content', ]
