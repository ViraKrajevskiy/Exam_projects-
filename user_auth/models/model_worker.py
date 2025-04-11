from django.db import models
from .auth_user import *
from .model_courses import *


class Staff(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departments = models.ManyToManyField('Departments', related_name='worker')
    course = models.ManyToManyField(, related_name='worker')
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.user.phone


class Departments(BaseModel):
    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    descriptions = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title