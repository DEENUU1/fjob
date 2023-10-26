from rest_framework import serializers
from .models import ReportMessage


class CreateReportMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportMessage
        fields = ["message", "offer", "user"]
