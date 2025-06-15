import string
import random
from django.db import models
from django.conf import settings
from user.models import User
from passage.models import Passage

def generate_unique_id():
    chars = string.ascii_uppercase + string.digits
    while True:
        new_id = ''.join(random.choices(chars, k=9))
        if not Ticket.objects.filter(id=new_id).exists():
            return new_id

class Ticket(models.Model):
    id = models.CharField(primary_key=True, max_length=9, editable=False, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tickets')
    passage_id = models.ForeignKey(Passage, on_delete=models.CASCADE, null=True)
    purchase_date = models.DateField(auto_now_add=True)
    purchase_time = models.TimeField(auto_now_add=True)
    PAYMENT_METHOD = [
        ('Pix', 'Pix'),
        ('Boleto', 'Boleto'),
        ('Débito', 'Débito'),
        ('Crédito', 'Crédito'),
    ]
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD)
    destination = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = generate_unique_id()
        super().save(*args, **kwargs)