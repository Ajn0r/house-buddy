from .models import Categories
from django import forms


class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ('name', 'slug')
