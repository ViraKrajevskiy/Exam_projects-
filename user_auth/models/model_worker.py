from django.db import models
from django.utils import timezone
from .model_student import *
from .user import *
from .model_courses import *

class WorkDay(models.Model):
    DAYS_OF_WEEK = [
        ('mon', 'Понедельник'),
        ('tue', 'Вторник'),
        ('wed', 'Среда'),
        ('thu', 'Четверг'),
        ('fri', 'Пятница'),
        ('sat', 'Суббота'),
        ('sun', 'Воскресенье'),
    ]

    code = models.CharField(max_length=3, choices=DAYS_OF_WEEK, unique=True)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class PositionLevel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Department(BaseModel):
    name = models.CharField(max_length=100)
    count_personal = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.count_personal} персонала)"

class WorkerSalaryPayed(BaseModel):
    total_amount_payed = models.IntegerField()
    datePayDay = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Оплачено: {self.total_amount_payed} в {self.datePayDay}"

class WorkerSalaryWaitedPay(BaseModel):
    worker = models.ForeignKey('Staff', on_delete=models.CASCADE, related_name='waiting_salaries', null=True, blank=True)
    total_amount = models.IntegerField()
    didnt_payed_days = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Ожидается: {self.total_amount} до {self.didnt_payed_days}"

class Staff(BaseModel):
    firstname = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    live_place_address = models.TextField(max_length=100)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='workers')
    salary_pay = models.OneToOneField(WorkerSalaryPayed, on_delete=models.CASCADE)
    position = models.ForeignKey(PositionLevel, on_delete=models.SET_NULL, null=True, blank=True)
    work_days = models.ManyToManyField(WorkDay, blank=True, related_name='staff_members')

    def __str__(self):
        return f"{self.firstname} {self.surname} - {self.position}"
