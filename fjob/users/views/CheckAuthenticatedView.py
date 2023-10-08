from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CheckAuthenticatedView(APIView):
    def get(self, request):
        user = self.request.user

        try:
            isAuthenticated = user.is_authenticated

            if isAuthenticated:
                return Response(
                    {"isAuthenticated": "success"}, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"isAuthenticated": "error"}, status=status.HTTP_403_FORBIDDEN
                )
        except:
            return Response(
                {"error": "Something went wrong when checking authentication status"},
                status=status.HTTP_403_FORBIDDEN,
            )
