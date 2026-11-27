from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filter import VesselFilter
from vessel.models import Vessel
from .serializers import VesselSerializer
from core.permissions import IsOwnerOrReadOnly, PublicReadOnly


class VesselViewSet(viewsets.ModelViewSet):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = VesselFilter

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsOwnerOrReadOnly()]
        return [PublicReadOnly()]

    def perform_create(self, serializer):
        # Set owner to the authenticated user
        serializer.save(owner=self.request.user)