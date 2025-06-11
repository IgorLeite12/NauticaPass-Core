from django.contrib.auth.models import AbstractUser
from django.db import models


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
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True,
                           error_messages={
                               'unique': 'Este CPF já está sendo usado.'
                           })
    rg = models.CharField(max_length=20, unique=True, blank=True, null=True)
    passport = models.CharField(max_length=20, unique=True, blank=True, null=True)
    GENDER_CHOICES = [
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('outro', 'Outro'),
    ]
    gender_type = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    NATIONALITY_CHOICE = [
        ('brasileiro', 'Brasileiro'),
        ('estrangeiro', 'Estrangeiro'),
    ]
    nationality_type = models.CharField(max_length=11, choices=NATIONALITY_CHOICE, blank=True, null=True)
