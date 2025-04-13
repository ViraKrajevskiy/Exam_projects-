from .model_teacher import *
from user_auth.models import BaseModel
from django.db import models

class StudyDay(models.Model):
    Course_Days = [
        ('mon', 'Понедельник'),
        ('tue', 'Вторник'),
        ('wed', 'Среда'),
        ('thu', 'Четверг'),
        ('fri', 'Пятница'),
        ('sat', 'Суббота'),
        ('sun', 'Воскресенье'),
    ]
    code = models.CharField(max_length=3, choices=Course_Days, unique=True)
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class CourseDuration(BaseModel):
    total_duration = models.IntegerField()
    course_start_time = models.DateField()
    course_end_time = models.DateField()
    work_days = models.ManyToManyField(StudyDay, related_name='course_durations')


class Course(BaseModel):
    course_cost_per_week = models.IntegerField()
    course_total_cost = models.IntegerField()
    course_name = models.CharField(max_length=90)
    course_descriptions = models.TextField(max_length=150)

    students = models.ManyToManyField('Student', related_name='courses', blank=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, related_name='courses')
    mentor = models.ForeignKey('Mentor', on_delete=models.SET_NULL, null=True, related_name='courses')

    course_duration = models.OneToOneField(CourseDuration, on_delete=models.CASCADE, related_name='course')
