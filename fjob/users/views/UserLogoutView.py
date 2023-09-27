from django.contrib.auth import get_user_model, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status


UserModel = get_user_model()


class UserLogoutView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
