from django_filters import rest_framework as filters
from .models import CarModel


class CarFilter(filters.FilterSet):
    price_lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    price_gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    brand_contains = filters.CharFilter(field_name='brand', lookup_expr='contains')
    brand_start = filters.CharFilter(field_name='brand', lookup_expr='istartswith')
    brand_end = filters.CharFilter(field_name='brand', lookup_expr='iendswith')
    year_lt = filters.NumberFilter(field_name='year_release', lookup_expr='lt')
    year_gt = filters.NumberFilter(field_name='year_release', lookup_expr='gt')
    year_gte = filters.NumberFilter(field_name='year_release', lookup_expr='gte')

    class Meta:
        model = CarModel
        fields = ('price_lt', 'price_gt', 'price_gte', 'brand_contains', 'brand_start', 'brand_end')
