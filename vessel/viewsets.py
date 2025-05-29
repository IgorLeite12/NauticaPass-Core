from rest_framework import viewsets
from user.models import Vessel
from .serializers import VesselSerializer

class VesselViewSet(viewsets.ModelViewSet):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer