import django_filters
from django_filters import DateFilter

from .models import Record

class OrderFilter(django_filters.FilterSet):
    # Iterate over field 'created_at'
    start_date = DateFilter(field_name="created_at", lookup_expr="gte")
    end_date = DateFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        model = Record
        fields = []
        # Don't show
