from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import UserPackage, Package


class GetUserFreeUses(APIView):
    authentication_classes = [
        SessionAuthentication,
    ]

    def get(self, request):
        user = request.user
        package = Package.objects.get(id=1)
        user_package = UserPackage.objects.filter(user=user, active=True).first()
        if user_package.package == package:
            return Response(
                {"free_uses": user_package.free_users},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"free_uses": None},
                status=status.HTTP_200_OK,
            )
