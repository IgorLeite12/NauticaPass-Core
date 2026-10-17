from django.db import models
from account.models import Account
from core.models import BaseModel


class Vessel(BaseModel):
    name_vessel = models.CharField(
        max_length=50,
        blank=False
    )

    owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='vessels'
    )

    capacity = models.PositiveIntegerField(
        blank=False,
    )
    
    NAVIGATION_TYPE_CHOICES = [
        ('barco', 'Barco'),
        ('ajato', 'Ajato'),
        ('balsa', 'Balsa'),
        ('ferry_boat', 'Ferry boat'),
    ]
    
    navigation_type = models.CharField(
        max_length=50,
        choices=NAVIGATION_TYPE_CHOICES,
        blank=True
    )
    
    def __str__(self):
        return f"Vessel: {self.name_vessel} - Owner: {self.owner} - Navigation Type: {self.navigation_type} - Capacity: {self.capacity}"
