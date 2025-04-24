from rest_framework import serializers
from user_auth.models.base_user_model.user import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['phone_number', 'email', 'password', 'role']

    def create(self, validated_data):
        # Извлекаем пароль из данных
        password = validated_data.pop('password')

        # Создаем нового пользователя, пароль будет автоматически хэширован
        user = User.objects.create_user(password=password, **validated_data)

        return user
