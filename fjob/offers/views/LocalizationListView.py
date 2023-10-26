from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from ..serializers.LocalizationCountrySerializer import LocalizationCountrySerializer
from ..models import Localization


class LocalizationListView(ListAPIView):
    serializer_class = LocalizationCountrySerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Localization.objects.values("country").distinct()
