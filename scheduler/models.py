# ai/models.py
from django.db import models
from ticket.models import Ticket

class Schedule(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE, related_name='schedule')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)