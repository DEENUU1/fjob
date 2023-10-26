from ..models import Localization
from rest_framework import serializers


class LocalizationCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Localization
        fields = ("country",)
