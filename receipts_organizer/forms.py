from .models import Categories, Entries
from django import forms


class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ('name', 'slug')


class NewEntryForm(forms.Form):
    class Meta:
        model = Entries