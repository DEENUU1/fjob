from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from payment.models import Package
from payment.serializers import PackageSerializer


class GetPackages(ListAPIView):
    serializer_class = PackageSerializer.PackageSerializer
    # authentication_classes = (SessionAuthentication,)
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        queryset = Package.objects.all()
        return queryset
