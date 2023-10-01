from rest_framework import serializers

from .models import Package


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = (
            "name",
            "price",
            "has_signals",
            "num_of_signals",
            "free_users",
        )
