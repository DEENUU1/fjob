from rest_framework import serializers

from .models import offers, salaries


class SalariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = salaries.Salaries
        fields = "__all__"


class OffersSerializer(serializers.ModelSerializer):
    salary = SalariesSerializer(many=True, read_only=True)
    is_new_offer = serializers.ReadOnlyField(source="is_new")

    class Meta:
        model = offers.Offers
        fields = "__all__"
