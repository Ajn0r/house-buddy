from django.forms import ModelForm
from . models import Comments


class CommentForm(ModelForm):
    """
    A form for Comments
    """
    class Meta:
        model = Comments
        fields = ['content', ]
