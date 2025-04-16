from user_auth.models import BaseModel
from django.core.exceptions import ValidationError
from user_auth.models.student_package.model_group import *


def validate_video_size(file):
    max_size_mb = 200
    if file.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Максимальный размер файла — {max_size_mb} МБ")


class GroupHomework(BaseModel):
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='homeworks')
    title = models.CharField(max_length=255)
    video_lesson = models.FileField(upload_to='video_lessons/',null=True,blank=True,validators=[validate_video_size] )
    description = models.TextField()
    deadline = models.DateTimeField()

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} (для {self.group.title})"

class StudentHomework(BaseModel):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='student_homeworks')
    group_homework = models.ForeignKey('GroupHomework', on_delete=models.CASCADE, related_name='student_homeworks')
    file = models.FileField(upload_to='homeworks/', blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_checked = models.BooleanField(default=False)
    mark = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.surname} - {self.group_homework.title}"
