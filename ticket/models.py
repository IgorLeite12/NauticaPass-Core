from django.db import models
from core.models import BaseModel
from passage.models import Passage
from account.models import Account 


from django.db import models
from django.core.exceptions import ValidationError


class Ticket(BaseModel):
    PAYMENT_METHOD = [
        ("pix", "Pix"),
        ("dinheiro", "Dinheiro"),
        ("cartao", "Cartão"),
    ]

    FORM_OF_PAYMENT_CARD = [
        ("credito", "Crédito"),
        ("debito", "Débito"),
    ]

    account = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name="tickets",
    )

    passage = models.ForeignKey(
        Passage,
        on_delete=models.PROTECT,
        related_name="tickets",
    )

    purchase_datetime = models.DateTimeField(
        auto_now_add=True
    )

    payment_method = models.CharField(
        max_length=10,
        choices=PAYMENT_METHOD,
    )

    subtype_card = models.CharField(
        max_length=10,
        choices=FORM_OF_PAYMENT_CARD,
        blank=True,
    )

    def clean(self):
        super().clean()

        if self.payment_method == "cartao" and not self.subtype_card:
            raise ValidationError({
                "subtype_card": "Informe crédito ou débito para pagamentos com cartão."
            })

        if self.payment_method != "cartao" and self.subtype_card:
            raise ValidationError({
                "subtype_card": "O subtipo só deve ser informado para pagamentos com cartão."
            })


    def __str__(self):
        return f"Ticket {self.pk} - {self.account} - {self.passage}"

