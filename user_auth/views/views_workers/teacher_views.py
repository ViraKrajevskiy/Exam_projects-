# views.py
from rest_framework import viewsets
from user_auth.models.workers_models.model_teacher import *
from user_auth.serializers.stafff_serializer.staff import *

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
