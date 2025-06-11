from django.db import models

class Vessel(models.Model):
    name_vessel = models.CharField(max_length=255, unique=True, blank=True)
    name_owner = models.CharField(max_length=255, blank=True)
    capacity = models.PositiveIntegerField(blank=True, null=True)
    NAVIGATION_TYPE_CHOICES = [
        ('barco', 'Barco'),
        ('ajato', 'Ajato'),
        ('balsa', 'Balsa'),
        ('ferry_boat', 'Ferry boat'),
    ]
    navigation_type = models.CharField(max_length=50, choices=NAVIGATION_TYPE_CHOICES, blank=True)
