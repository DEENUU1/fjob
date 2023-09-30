from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from ..serializers import UserPasswordChangeSerializer


UserModel = get_user_model()


class UserPasswordChangeView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserPasswordChangeSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"detail": "Password changed successfully"},
                status=status.HTTP_200_OK,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
