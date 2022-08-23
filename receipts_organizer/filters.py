import django_filters
from .models import Entries
from django_filters.widgets import RangeWidget
from django_filters import DateFromToRangeFilter

class EntryFilter(django_filters.FilterSet):
    """
    Filter class for filtering entries
    """
    title = django_filters.CharFilter(lookup_expr='icontains')
    date_of_purchase = DateFromToRangeFilter(
        widget=RangeWidget(attrs={
            'placeholder': 'YYYY/MM/DD', 'type': 'date', 'class': 'w-50 form-control'}))

    class Meta:
        model = Entries
        fields = ['title', 'date_of_purchase']
