from django_filters import rest_framework as filters
from .models import AutoParksModel
class AutoParkCarsFilter(filters.FilterSet):
    year_lt = filters.NumberFilter(field_name='cars__year_release', lookup_expr='lt')

    class Meta:
        model = AutoParksModel
        fields = ('year_lt',)
