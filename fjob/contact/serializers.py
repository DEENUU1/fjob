import re

from rest_framework import serializers

from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Contact

    def validate(self, data):
        email = data.get("email")

        if not data.get("name"):
            raise serializers.ValidationError("No name provided")
        if not email:
            raise serializers.ValidationError("No email provided")
        if not data.get("content"):
            raise serializers.ValidationError("No content provided")

        if not re.match(r"^[\w\.-]+@[\w\.-]+$", email):
            raise serializers.ValidationError("Invalid email address")

        return data

    def create(self, validated_data):
        return Contact.objects.create(**validated_data)
