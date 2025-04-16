from django.db import models
from rest_framework.fields import DateTimeField
from user_auth.models.base_user_model.user import BaseModel
from user_auth.models.workers_models.model_worker import Staff


class PyedForWorker(BaseModel):
    card_number = models.IntegerField(max_length=16,unique=True)
    work_time = models.DateTimeField(auto_now_add=True)
    balance = models.OneToOneField(Staff,on_delete=models.CASCADE)