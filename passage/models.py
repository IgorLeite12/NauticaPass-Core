from django.db import models
from core.models import BaseModel
from vessel.models import Vessel
from account.models import City

class Passage(BaseModel):
    vessel = models.ForeignKey(
        Vessel,
        on_delete=models.CASCADE
    )
    origin = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="origem_passagem"
    )
    destination = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="destino_passagem"
    )
    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    capacity = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.origin} → {self.destination} - {self.vessel}"
