from rest_framework import serializers
from django.contrib.auth import authenticate
from user_auth.models.base_user_model.user import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['phone_number', 'email', 'password', 'role']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(phone_number=data['phone_number'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Неверный номер телефона или пароль')
        if not user.is_active:
            raise serializers.ValidationError('Пользователь деактивирован')
        data['user'] = user
        return data
