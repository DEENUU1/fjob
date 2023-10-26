from rest_framework import serializers
from ..models import Salaries
from ..serializers import WorkScheduleSerializer, ContractTypeSerializer


class SalariesSerializer(serializers.ModelSerializer):
    work_schedule = WorkScheduleSerializer.WorkScheduleSerializer(many=True)
    contract_type = ContractTypeSerializer.ContractTypeSerializer(many=True)

    class Meta:
        model = Salaries
        fields = "__all__"
