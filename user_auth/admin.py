from django.contrib import admin
from .models import *

admin.site.register([StudyDay,User,Teacher,CourseDuration, Student,PositionLevel,WorkDay,WorkerSalaryPayed,WorkerSalaryWaitedPay,Course,Staff, Department,Parents, GroupHomework,StudentHomework,Mentor,Group,Lesson,Room])