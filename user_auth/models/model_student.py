from django.db import models
from .user import User
from .model_courses import *
from .model_teacher import *
from .model_worker import *

class Student(models.Model):
    surname = models.CharField(30)
    firstname = models.CharField(30)
    lastname = models.CharField(30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ManyToManyField('Group', related_name='student')
    is_line = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.surname},{self.firstname},{self.lastname},{self.group}"


class Parents(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    descriptions = models.CharField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} ({self.phone_number})"
