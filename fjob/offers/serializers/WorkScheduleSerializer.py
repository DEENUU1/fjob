from rest_framework import serializers
from ..models import WorkSchedule


class WorkScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSchedule
        fields = "__all__"
