from django_filters import rest_framework as filters
from .models import Vessel


class VesselFilter(filters.FilterSet):
    name_vessel = filters.CharFilter(field_name='name_vessel', lookup_expr='icontains')
    name_owner = filters.CharFilter(field_name='name_owner', lookup_expr='icontains')
    navigation_type = filters.CharFilter(field_name='navigation_type', lookup_expr='icontains')


    class Meta:
        model = Vessel
        fields = ['name_vessel', 'name_owner', 'navigation_type']