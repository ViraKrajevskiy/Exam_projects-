from user_auth.models import BaseModel
from django.db import models

class PayedProgram(BaseModel):
    programs = [
        ('Cl','Click'),
        ('pay','PayMe'),
        ('Uzu','UzumBank'),
    ]


# class StudentPay(BaseModel):
#     money