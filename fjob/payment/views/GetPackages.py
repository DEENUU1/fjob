from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from ..models import Package
from ..serializers import PackageSerializer


class GetPackages(ListAPIView):
    serializer_class = PackageSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        queryset = Package.objects.all()
        return queryset
