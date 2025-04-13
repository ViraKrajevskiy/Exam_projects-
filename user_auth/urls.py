from django.urls import path,include
from rest_framework.routers import DefaultRouter
from user_auth.views.user_api import RegisterUserApi

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('userApi/', RegisterUserApi.as_view()),
]