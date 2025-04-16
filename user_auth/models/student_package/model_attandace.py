from user_auth.models.base_user_model.user import BaseModel
from django.db import models

from user_auth.models.student_package.model_group import Group
from user_auth.models.student_package.model_student import Student


class Attendance(models.Model):
    ATTENDANCE_STATUS_CHOICES = [
        ('P', 'Пришел'),
        ('A', 'Отсутствует'),
        ('L', 'Опоздал'),
        ('E', 'Уважительная причина'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    status = models.CharField(max_length=1, choices=ATTENDANCE_STATUS_CHOICES)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='attendances')

    class Meta:
        unique_together = ['student', 'date']

    def __str__(self):
        return f"{self.student} - {self.date} - {self.get_status_display()}"