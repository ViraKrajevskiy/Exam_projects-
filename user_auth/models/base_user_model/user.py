from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class BaseModel(models.Model):
    created_ed = models.DateField(auto_now_add=True)
    updated_ed = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, email=None, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Поле ввода номера телефона не должно быть пустым!')
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, email=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True!')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True!')

        return self.create_user(phone_number, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Админ'
        STUDENT = 'student', 'Студент'
        TEACHER = 'teacher', 'Преподаватель'
        WORKER = 'worker', 'Сотрудник'

    phone_regex = RegexValidator(
        regex=r'^\+998\d{9}$',
        message="Номер телефона должен быть в формате +998XXXXXXXX!"
    )
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=13, unique=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number
