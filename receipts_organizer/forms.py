from .models import Categories, Entries
from django import forms

class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name', ]

class NewEntryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        self.request = kwargs.pop('request')
        super(NewEntryForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Categories.objects.filter(user=self.request.user)

    class Meta:
        model = Entries
        fields = [
            'title', 'category', 'image', 
            'amount', 'date_of_purchase', 'description'
            ]

        widgets = {
            'date_of_purchase': forms.DateInput(format="%m/%d/%Y", attrs={'type': 'date'})
        }
