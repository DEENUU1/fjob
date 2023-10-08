from django.contrib.auth import get_user_model, logout
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


UserModel = get_user_model()


class UserLogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            logout(request)
            return Response({"message": "Ok"}, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)
