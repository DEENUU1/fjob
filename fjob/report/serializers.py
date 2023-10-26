from rest_framework import serializers
from .models import ReportMessage


class ReportMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportMessage
        fields = "__all__"
