from user_auth.views import *
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import  DefaultRouter


router=DefaultRouter()


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("",include(router.urls)),
    path('teacher_api/',TeacherViewSet.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]