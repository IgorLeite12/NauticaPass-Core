from rest_framework.generics import ListAPIView
from user.models import Passage, City
from .serializers import PassageSerializer, CitySerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class PassageViewSet(viewsets.ModelViewSet):
    queryset = Passage.objects.all()
    serializer_class = PassageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['origin', 'destination', 'value']


class CityListView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
