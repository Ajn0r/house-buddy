from . models import Comments, Blogpost
from django.forms import ModelForm


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['content', ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CommentForm, self).__init__(*args, **kwargs)


    