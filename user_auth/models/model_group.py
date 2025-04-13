from rest_framework.fields import CharField

from user_auth.models import BaseModel
from django.db import models

class Group(BaseModel):
    group_name = models.CharField(max_length=90)

