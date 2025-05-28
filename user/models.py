from hashid_field import HashidAutoField
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True)
    cpf = models.CharField(max_length=14, unique=True)
    birth_date = models.DateField(null=True, blank=True)

class Ticket(models.Model):
    id = HashidAutoField(primary_key=True,
                         min_length=9,
                         alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
                         )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    purchase_date = models.DateField()
    travel_date = models.DateField()
    purchase_time = models.TimeField()
    travel_time = models.TimeField()

    NAVIGATION_TYPE_CHOICES = [
        ('barco', 'Barco'),
        ('ajato', 'Ajato'),
        ('balsa', 'Balsa'),
        ('ferry_boat', 'Ferry boat'),
    ]
    navigation_type = models.CharField(max_length=50, choices=NAVIGATION_TYPE_CHOICES)

    def __str__(self):
        return f'{self.id} - {self.origin} to {self.destination}'