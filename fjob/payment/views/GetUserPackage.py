from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import UserPackage, Package
from rest_framework.authentication import SessionAuthentication


class GetUserPackage(APIView):
    authentication_classes = [
        SessionAuthentication,
    ]

    def get(self, request):
        user = self.request.user
        user_package = UserPackage.objects.filter(user=user, active=True).first()

        package = user_package.package if user_package else None

        if not package:
            return Response(
                {"message": "No package found"}, status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            {"name": package.name, "price": package.price}, status=status.HTTP_200_OK
        )
