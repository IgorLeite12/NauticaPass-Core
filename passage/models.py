from django.db import models
from django.core.validators import MinValueValidator
from core.models import BaseModel
from vessel.models import Vessel
from account.models import City

class Passage(BaseModel):
    vessel = models.ForeignKey(
        Vessel,
        on_delete=models.PROTECT,
        related_name="passages"
    )
    
    origin = models.ForeignKey(
        City,
        on_delete=models.PROTECT,
        related_name="origin_passage"
    )
    
    destination = models.ForeignKey(
        City,
        on_delete=models.PROTECT,
        related_name="destination_passage"
    )
    
    value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    def __str__(self):
        return (
            f"{self.origin} → {self.destination} "
            f"- Vessel: {self.vessel} "
            f"- Price: R$ {self.value:.2f}"
        )