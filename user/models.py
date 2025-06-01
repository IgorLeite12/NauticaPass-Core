from hashid_field import HashidAutoField
from django.contrib.auth.models import AbstractUser
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class User(AbstractUser):
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'Este email já está sendo usado.'
        }
    )
    phone = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
    rg = models.CharField(max_length=20, unique=True, blank=True, null=True)


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


class Passage(models.Model):
    id_vessel = models.ForeignKey(Vessel, on_delete=models.CASCADE, related_name='passages_as_vessel', null=True, blank=True)
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

class Ticket(models.Model):
    id = HashidAutoField(primary_key=True, min_length=9, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    passage_id = models.ForeignKey(Passage, on_delete=models.CASCADE, null=True)
    purchase_date = models.DateField()
    purchase_time = models.TimeField()
    PAYMENT_METHOD = [
        ('pix', 'Pix'),
        ('cash', 'Boleto'),
    ]
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD)