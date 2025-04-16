from django.db import models
from user_auth.models.base_user_model.user import BaseModel

class StudentPay(BaseModel):
    PAYMENT_TYPE_CHOICES = [
        ('Cr', 'Картой'),
        ('Mn', 'Наличкой'),
    ]

    payment_type = models.CharField(choices=PAYMENT_TYPE_CHOICES, max_length=2)
    value = models.IntegerField()
    card_num = models.CharField(max_length=16, blank=True, null=True)  # Только если тип оплаты "Cr"

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.payment_type == 'Cr' and not self.card_num:
            raise ValidationError("Номер карты обязателен для оплаты картой.")
        if self.payment_type == 'Mn' and self.card_num:
            raise ValidationError("Номер карты не должен быть указан для наличной оплаты.")

