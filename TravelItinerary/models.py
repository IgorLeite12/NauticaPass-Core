from django.db import models
from ticket.models import Ticket
from django.conf import settings

class TravelItinerary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='itineraries')
    passage = models.OneToOneField(
        Ticket,
        on_delete=models.CASCADE,
        related_name='itinerary',
        verbose_name='Passagem'
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)