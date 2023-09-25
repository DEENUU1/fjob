from rest_framework import serializers
from .models import Offers, Salaries


class SalariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salaries
        fields = "__all__"


class OffersSerializer(serializers.ModelSerializer):
    salary = SalariesSerializer(many=True, read_only=True)

    class Meta:
        model = Offers
        fields = "__all__"
