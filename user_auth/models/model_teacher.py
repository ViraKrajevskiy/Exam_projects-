from django.db import models

from user_auth.models import BaseModel


class Course(BaseModel):
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title

class Teacher(BaseModel):
    name