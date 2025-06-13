import string
import random
from django.db import models
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
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    passage_id = models.ForeignKey(Passage, on_delete=models.CASCADE, null=True)
    purchase_date = models.DateField()
    purchase_time = models.TimeField()
    PAYMENT_METHOD = [
        ('pix', 'Pix'),
        ('cash', 'Boleto'),
    ]
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = generate_unique_id()
        if self.passage_id:
            self.origin = self.passage_id.origin.name
            self.destination = self.passage_id.destination.name
        super().save(*args, **kwargs)