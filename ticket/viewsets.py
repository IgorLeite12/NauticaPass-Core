from rest_framework import viewsets
from user.models import Ticket
from .serializers import TicketSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    http_method_names = ['get', 'post', 'patch']
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['user', 'origin', 'destination', 'navigation_type']
    ordering_fields = ['purchase_date', 'travel_date']
    ordering = ['travel_date']