from django.db import models
from hashid_field import HashidAutoField
from user.models import User
from passage.models import Passage

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