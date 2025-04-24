from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from user_auth.models.base_user_model.user import User

class CustomLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = User.objects.filter(phone_number=data['phone_number']).first()

        if not user:
            raise serializers.ValidationError("Неверный номер телефона или пароль")

        if not user.check_password(data['password']):
            raise serializers.ValidationError("Неверный номер телефона или пароль")

        if not user.is_active:
            raise serializers.ValidationError("Пользователь деактивирован")

        # Generate JWT tokens (Access & Refresh)
        refresh = RefreshToken.for_user(user)
        data['access_token'] = str(refresh.access_token)
        data['refresh_token'] = str(refresh)

        return data
