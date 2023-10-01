from django.contrib.auth import get_user_model, login
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import UserLoginSerializer

UserModel = get_user_model()


class UserLoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)

        if serializer.is_valid():
            user = serializer.check_user(validated_data=data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(
            {"detail": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST
        )
