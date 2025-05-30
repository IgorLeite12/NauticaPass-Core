from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from user.models import Vessel
from .serializers import VesselSerializer

class VesselViewSet(viewsets.ModelViewSet):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name_vessel',
                        'name_owner',
                        'navigation_type']