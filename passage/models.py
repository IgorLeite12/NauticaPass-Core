from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
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
    
    departure_time = models.DateTimeField(
        blank=False,
    )
    
    arrival_time = models.DateTimeField(
        blank=False,
    )
    
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    
    available_seats = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    
    """ Salva a disponibilidade de cadeiras com base na capacidade do navio, caso não seja fornecida. """
    def save(self, *args, **kwargs):
        if self.available_seats is None:
            self.available_seats = self.vessel.capacity
            
        super(Passage, self).save(*args, **kwargs)
        
        
    def clean(self):
        super().clean()

        if (
            self.departure_time
            and self.arrival_time
            and self.arrival_time <= self.departure_time
        ):
            raise ValidationError({
                "arrival_time": "A chegada deve ocorrer após a partida."
            })

        if self.origin_id and self.destination_id:
            if self.origin_id == self.destination_id:
                raise ValidationError({
                    "destination": "A origem e o destino devem ser diferentes."
                })
    

    def __str__(self):
        return (
            f"{self.origin} → {self.destination} "
            f"- Vessel: {self.vessel} "
            f"- Price: R$ {self.price:.2f}"
        )