from rest_framework import serializers
from ..models import Offers
from .WebsiteSerializer import WebsiteSerializer
from .ExperienceLevelSerializer import ExperienceLevelSerializer
from .SalariesSerializer import SalariesSerializer
from .LocalizationSerializer import LocalizationSerializer


class OffersSerializer(serializers.ModelSerializer):
    website = WebsiteSerializer()
    experience_level = ExperienceLevelSerializer(many=True)
    salary = SalariesSerializer(many=True)
    localizations = LocalizationSerializer(many=True)
    is_new = serializers.ReadOnlyField()

    class Meta:
        model = Offers
        fields = "__all__"
