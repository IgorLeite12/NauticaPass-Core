from rest_framework import viewsets
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from user.permissions import IsProprietario
from vessel.models import Vessel
from .serializers import VesselSerializer



class VesselFilter(filters.FilterSet):
    name_vessel = filters.CharFilter(field_name='name_vessel', lookup_expr='icontains')
    name_owner = filters.CharFilter(field_name='name_owner', lookup_expr='icontains')
    capacity = filters.CharFilter(field_name='capacity', lookup_expr='icontains')  # Corrigido aqui
    navigation_type = filters.CharFilter(field_name='navigation_type', lookup_expr='icontains')

    class Meta:
        model = Vessel
        fields = ['name_vessel', 'name_owner', 'capacity', 'navigation_type']


class VesselViewSet(viewsets.ModelViewSet):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class =   VesselFilter
    permission_classes = [IsProprietario]
