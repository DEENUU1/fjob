from django.contrib.auth import get_user_model, login
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserLoginSerializer


UserModel = get_user_model()


class UserLoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    serializer_class = UserLoginSerializer.UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data["user"]
            login(request, user)
            return Response({"message": "ok"}, status=status.HTTP_200_OK)

        raise AuthenticationFailed("Invalid credentials")
