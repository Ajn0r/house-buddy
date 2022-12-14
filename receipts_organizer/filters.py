import django_filters
from django_filters import DateFromToRangeFilter, RangeFilter
from django_filters.widgets import RangeWidget
from .models import Entries


class EntryFilter(django_filters.FilterSet):
    """
    Filter class for filtering entries
    """
    title = django_filters.CharFilter(lookup_expr='icontains')
    date_of_purchase = DateFromToRangeFilter(
        widget=RangeWidget(attrs={
            'type': 'date', 'class': 'col-sm-5'})
    )
    amount = RangeFilter(
        widget=RangeWidget(attrs={
            'class': 'col-sm-5'})
    )

    class Meta:
        model = Entries
        fields = ['title', 'amount', 'date_of_purchase']
