from rest_framework import serializers
from ..models import Salaries


class SalariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salaries
        fields = "__all__"
