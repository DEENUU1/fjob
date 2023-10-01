from rest_framework.response import Response
from rest_framework.views import APIView


class CancelView(APIView):
    def get(self, request):
        return Response({"cancelled": True})
