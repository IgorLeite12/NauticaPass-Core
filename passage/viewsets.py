from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import BasePermission, SAFE_METHODS, AllowAny, IsAuthenticated
from passage.models import Passage, City
from user.permissions import IsProprietarioOrReadOnly
from .serializers import PassageSerializer, CitySerializer


class PassageFilter(DjangoFilterBackend):
    origin = filters.CharFilter(field_name='origin', lookup_expr='icontains')
    destination = filters.CharFilter(field_name='destination', lookup_expr='icontains')
    value = filters.CharFilter(field_name='value', lookup_expr='icontains')

    class Meta:
        model = Passage
        fields = ['origin', 'destination', 'value']


class ReadOnlyOrAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

class PassageViewSet(viewsets.ModelViewSet):
    queryset = Passage.objects.all()
    serializer_class = PassageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['origin', 'destination', 'travel_date', 'value']
    permission_classes = [IsProprietarioOrReadOnly]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]


class CityListView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    pagination_class = None
