from rest_framework.serializers import ModelSerializer
from .models import Report


class ReportSerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"
