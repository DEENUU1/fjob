from rest_framework import serializers
from ..models import ExperienceLevel


class ExperienceLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceLevel
        fields = "__all__"
