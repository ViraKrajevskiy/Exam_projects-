from django.db import models
from .model_group import *
from user_auth.models import BaseModel
from .model_worker import *


class Teacher(BaseModel):
    staff = models.OneToOneField('Staff', on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    teacher_group = models.ManyToManyField(Group, related_name='teachers')


class Mentor(BaseModel):
    staff = models.OneToOneField('Staff', on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    mentor_group = models.ManyToManyField(Group, related_name='mentors')
