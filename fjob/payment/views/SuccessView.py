from rest_framework.response import Response
from rest_framework.views import APIView

from payment.models import UserPackage


class SuccessView(APIView):
    def get(self, request, custom_id):
        user_package = UserPackage.objects.filter(custom_id=custom_id).first()
        user_package.active = True
        user_package.save()
        UserPackage.objects.exclude(custom_id=custom_id).update(active=False)
        return Response({"success": True})
