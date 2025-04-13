from django.db import models
from .model_student import *
from .user import *
from .model_courses import *

class Staff:
    user = models.OneToOneField('User', on_delete=models.CASCADE)

class WorkerSalary: