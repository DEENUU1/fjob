from django.contrib.auth import get_user_model
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from ..serializers import ChangeEmailSerializer


UserModel = get_user_model()


class UserEmailChangeView(UpdateAPIView):
    serializer_class = ChangeEmailSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def update(self, request, *args, **kwargs):
        serializer = ChangeEmailSerializer(data=request.data)
        serializer.is_valid()

        user = self.request.user
        password = serializer.validated_data["password"]
        old_email = serializer.validated_data["old_email"]
        new_email = serializer.validated_data["new_email"]

        if UserModel.objects.filter(email=new_email).exists():
            return Response(
                {"detail": "Email already exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not user.check_password(password):
            return Response(
                {"detail": "Incorrect password."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not user.email == old_email:
            return Response(
                {"detail": "Incorrect old email."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if old_email == new_email:
            return Response(
                {"detail": "New email must be different from old email."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.email = new_email
        user.save()

        return Response(
            {"detail": "Email changed successfully."}, status=status.HTTP_200_OK
        )
