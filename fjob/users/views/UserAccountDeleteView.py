from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.serializers import AccountDeleteSerializer


UserModel = get_user_model()


class UserAccountDeleteView(DestroyAPIView):
    serializer_class = AccountDeleteSerializer
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (SessionAuthentication,)

    def delete(self, request, *args, **kwargs):
        serializer = AccountDeleteSerializer.AccountDeleteSerializer(data=request.data)
        serializer.is_valid()

        user = self.request.user

        if not user.check_password(serializer.validated_data["password"]):
            return Response(
                {"detail": "Incorrect password."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not user.email == serializer.validated_data["email"]:
            return Response(
                {"detail": "Incorrect email."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not user.username == serializer.validated_data["username"]:
            return Response(
                {"detail": "Incorrect username."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
