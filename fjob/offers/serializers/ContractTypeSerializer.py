from rest_framework import serializers
from ..models import ContractType


class ContractTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractType
        fields = "__all__"
