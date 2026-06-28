from django.db import models
from core.models import BaseModel
from passage.models import Passage
from account.models import Account 

class Ticket(BaseModel):
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        null=True
    )
    passage_id = models.ForeignKey(
        Passage,
        on_delete=models.CASCADE,
        null=True
    )
    purchase_date = models.DateField()
    purchase_time = models.TimeField()
    PAYMENT_METHOD = [
        ('pix', 'Pix'),
        ('cash', 'Boleto'),
    ]
    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHOD
    )
