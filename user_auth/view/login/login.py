# from rest_framework import viewsets, status
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.tokens import RefreshToken
#
# from user_auth.serializers.login_and_registration_serializer.logins_serializer import RegisterSerializer, LoginSerializer
#
# class AuthViewSet(viewsets.ViewSet):
#     permission_classes = [AllowAny]
#
#
#     @action(detail=False, methods=['post'], url_path='register')
#     def register(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({"message": "Пользователь успешно зарегистрирован!"}, status=status.HTTP_201_CREATED)
#
#     @action(detail=False, methods=['post'], url_path='login')
#     def login(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             user = serializer.validated_data['user']
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             })
#         else:
#             return Response({"error": "Invalid login credentials"}, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from user_auth.serializers.login_and_registration_serializer.logins_serializer import *
from user_auth.serializers.login_and_registration_serializer.registration_serializer import *
from rest_framework.decorators import action


def register_page(request):
    return render(request, 'login_registration/register_page.html')

def login_page(request):
    return render(request, 'login_registration/login_page.html')

class AuthViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'], url_path='register')
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"message": "Пользователь успешно зарегистрирован!"}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({"error": "Invalid login credentials"}, status=status.HTTP_400_BAD_REQUEST)
