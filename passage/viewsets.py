from user.models import Passage, City
from .serializers import PassageSerializer, CitySerializer
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

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

    # def get(self, request, *args, **kwargs):
    #     try:
    #         cities = self.get_queryset()
    #         serializer = self.get_serializer(cities, many=True)
    #         return Response({
    #             'status': 'success',
    #             'data': serializer.data,
    #             'count': cities.count()
    #         })
    #     except Exception as e:
    #         return Response({
    #             'status': 'error',
    #             'message': str(e)
    #         }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
