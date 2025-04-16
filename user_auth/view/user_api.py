# from drf_yasg.utils import swagger_auto_schema
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.response import Response
# from rest_framework.views_sets import APIView
# from user_auth.serializers.user_login.user_serializer import *
# from django.contrib.auth.hashers import make_password
#
#
# class RegisterUserApi(APIView):
#     pagination_class = PageNumberPagination
#
#     @swagger_auto_schema(request_body=UserSerializer)
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             password = serializer.validated_data.get('password')
#             serializer.validated_data['password'] = make_password(password)
#             serializer.save()
#             return Response({
#                 'status': True,
#                 'datail': 'Account create'
#             })
#
#     def get(self, request):
#         users = User.objects.all().order_by('-id')
#         serializer = UserSerializer(users, many=True)
#         return Response(data=serializer.data)
#
