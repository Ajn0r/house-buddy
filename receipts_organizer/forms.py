from .models import Categories, Entries
from django import forms
from django.forms import ValidationError


class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name', ]



class NewEntryForm(forms.Form):
    class Meta:
        model = Entries