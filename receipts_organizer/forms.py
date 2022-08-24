from datetime import date
from django import forms
from .models import Categories, Entries


class NewCategoryForm(forms.ModelForm):
    """
    Form for creating a new category
    """
    class Meta:
        model = Categories
        fields = ['name', ]

    def clean_name(self):
        """
        Takes the category name and turn it to lowercase
        Prevents user from having duplicate categories
        """
        return self.cleaned_data['name'].lower()


class NewEntryForm(forms.ModelForm):
    """
    Form for creating new entries.
    """
    def __init__(self, *args, **kwargs):
        """
        Function to only let the user choose from
        a list of their own categories
        """
        self.request = kwargs.pop('request')
        super(NewEntryForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Categories.objects.filter(
            user=self.request.user)

    class Meta:
        model = Entries
        fields = [
            'title', 'category', 'image',
            'amount', 'date_of_purchase', 'description'
            ]

        widgets = {
            'date_of_purchase': forms.DateInput(
                format="%m/%d/%Y", attrs={'type': 'date', 'max': date.today()},
            )
        }
