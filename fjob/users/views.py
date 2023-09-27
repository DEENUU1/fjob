from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import UserSerializer, UserRegisterSerializer, UserLoginSerializer

UserModel = get_user_model()


class UserRegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        serializer = UserRegisterSerializer(data=data)

        if serializer.is_valid():
            email = data.get("email")
            password = data.get("password")
            username = data.get("username")

            if UserModel.objects.filter(email=email).exists():
                return Response(
                    {"detail": "Email already exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            elif UserModel.objects.filter(username=username).exists():
                return Response(
                    {"detail": "Username already exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            elif len(password) < 6:
                return Response(
                    {"detail": "Password must be at least 6 characters"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user = serializer.create(data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(
            {"detail": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST
        )
