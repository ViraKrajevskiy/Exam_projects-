from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user_auth.models import User
from rest_framework import serializers

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)


        token['role'] = user.role
        token['phone_number'] = user.phone_number
        return token

    def validate(self, attrs):
        phone = attrs.get("username")
        password = attrs.get("password")

        try:
            user = User.objects.get(phone_number=phone)
        except User.DoesNotExist:
            raise serializers.ValidationError({"detail": "Пользователь не найден"})

        attrs["username"] = user.phone_number
        return super().validate(attrs)
