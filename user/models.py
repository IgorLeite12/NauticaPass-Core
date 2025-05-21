from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    cpf = models.CharField(max_length=14, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    password = models.CharField(max_length=128, default='')

    def __str__(self):
        return self.name