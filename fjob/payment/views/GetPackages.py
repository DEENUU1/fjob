from rest_framework.generics import ListAPIView
from ..models import Package
from ..serializers import PackageSerializer


class GetPackages(ListAPIView):
    serializer_class = PackageSerializer

    def get_queryset(self):
        queryset = Package.objects.all()
        return queryset
