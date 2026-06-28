from django.db import models
from account.models import Account
from core.models import BaseModel


class Vessel(BaseModel):
    name_vessel = models.CharField(
        max_length=50,
        unique=True,
        blank=True
    )
    name_owner = models.CharField(
        max_length=255,
        blank=True
    )
    owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='vessels'
    )

    capacity = models.PositiveIntegerField(
        blank=True,
        null=True
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
