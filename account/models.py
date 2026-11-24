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
    
    # Remove first_name and last_name fields from AbstractUser
    first_name=None
    last_name=None
    
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
        null=True,
        error_messages={
            'unique': messages.PHONE_IN_USING
        }
    )
    
    birth_date = models.DateField(
        null=True,
        blank=True
    )
    
    cpf = models.CharField(
        max_length=11,
        unique=True,
        blank=True,
        default="",
        error_messages={
            'unique': messages.CPF_IN_USING
        }
    )
