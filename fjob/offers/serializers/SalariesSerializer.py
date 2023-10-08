from rest_framework import serializers

from offers.models import salaries


class SalariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = salaries.Salaries
        fields = "__all__"
