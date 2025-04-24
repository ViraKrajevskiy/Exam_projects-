from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

class LogoutView(APIView):
    def post(self, request):
        return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)