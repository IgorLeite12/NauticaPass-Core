from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from user.models import Ticket
from .serializers import TicketSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    http_method_names = ['get', 'post', 'patch']
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['user', 'origin', 'destination', 'navigation_type']
    ordering_fields = ['purchase_date', 'travel_date']
    ordering = ['travel_date']
    permission_classes = [IsAuthenticated]
