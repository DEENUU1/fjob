from rest_framework import serializers
from ..models import Localization


class LocalizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localization
        fields = "__all__"
