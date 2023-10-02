from rest_framework import serializers

from .models import Package, UserPackage


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = (
            "name",
            "price",
            "has_signals",
            "num_of_signals",
        )


class UserPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPackage
        fields = (
            "user",
            "package",
            "active",
            "free_uses",
        )
