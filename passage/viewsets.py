from rest_framework.generics import ListAPIView
from passage.models import Passage, City
from .serializers import PassageSerializer, CitySerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from core.permissions import IsOwnerOnly


class PassageViewSet(viewsets.ModelViewSet):
    serializer_class = PassageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['origin', 'destination', 'price']
    permission_classes = [IsOwnerOnly]

    def get_queryset(self):
        # Return only passages where the user owns the vessel
        user = self.request.user
        return Passage.objects.filter(vessel__owner=user)


class CityListView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
