from django.contrib.auth import get_user_model
from rest_framework import status

# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from django.contrib import auth

UserModel = get_user_model()


class UserLogoutView(APIView):
    authentication_classes = [SessionAuthentication]

    def post(self, request):
        try:
            auth.logout(request)
            return Response({"message": "Ok"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)
