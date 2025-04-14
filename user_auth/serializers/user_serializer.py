from rest_framework import serializers
from user_auth.models.base_user_model.user import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'phone_number', 'password', "full_name", 'is_active', 'is_staff', "is_teacher", 'is_admin',"is_student")


