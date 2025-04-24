from rest_framework import serializers
from django.contrib.auth import authenticate
from user_auth.models.base_user_model.user import User


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        # Получаем пользователя по номеру телефона
        try:
            user = User.objects.get(phone_number=data['phone_number'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Неверный номер телефона или пароль")

        if not user.check_password(data['password']):
            raise serializers.ValidationError("Неверный номер телефона или пароль")

        if not user.is_active:
            raise serializers.ValidationError("Пользователь деактивирован")


        data['user'] = user
        return data
