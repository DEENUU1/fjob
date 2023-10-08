from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.serializers import ChangePasswordSerializer

UserModel = get_user_model()


class UserPasswordChangeView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer.ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.update_password(request.user)
            return Response({"message": "ok"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
