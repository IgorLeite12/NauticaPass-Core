from django.db import models
from account import messages
from core.models import BaseModel
from django.contrib.auth.models import AbstractUser

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Account(AbstractUser, BaseModel):
    name = models.CharField(
        max_length=255,
        blank=True
    )
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': messages.EMAIL_IN_USING
        }
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    birth_date = models.DateField(
        null=True,
        blank=True
    )
    cpf = models.CharField(
        max_length=14,
        unique=True,
        blank=False,
        null=True
    )
    rg = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True
    )
