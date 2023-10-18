from rest_framework.serializers import ModelSerializer
from .models import Report, UserStats


class ReportSerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"


class UserStatsSerializer(ModelSerializer):
    class Meta:
        model = UserStats
        fields = "__all__"
