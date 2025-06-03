from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters
from user.models import Passage, City
from .serializers import PassageSerializer, CitySerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class PassageFilter(DjangoFilterBackend):
    origin = filters.CharFilter(field_name='origin', lookup_expr='icontains')
    destination = filters.CharFilter(field_name='destination', lookup_expr='icontains')
    value = filters.CharFilter(field_name='value', lookup_expr='icontains')

    class Meta:
        model = Passage
        fields = ['origin', 'destination', 'value']

class PassageViewSet(viewsets.ModelViewSet):
    queryset = Passage.objects.all()
    serializer_class = PassageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['origin', 'destination', 'value']


class CityListView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    pagination_class = None
