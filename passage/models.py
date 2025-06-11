from django.db import models
from vessel.models import Vessel

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Passage(models.Model):
    id_vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE, related_name='passages_as_vessel', null=True)
    origin = models.ForeignKey(City, on_delete=models.CASCADE, related_name='passages_origin')
    destination = models.ForeignKey(City, on_delete=models.CASCADE, related_name='passages_destination')
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    capacity = models.PositiveIntegerField(null=True, blank=True)
    travel_date = models.DateField()
    departure_time = models.TimeField(blank=True, null=True)
    arrival_date = models.DateField()
    arrival_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.origin} → {self.destination} - {self.id_vessel}"