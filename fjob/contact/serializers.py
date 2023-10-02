from .models import Contact

from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Contact

    def validate(self, data):
        if not data:
            raise serializers.ValidationError("No data provided")
        if not data.get("name"):
            raise serializers.ValidationError("No name provided")
        if not data.get("email"):
            raise serializers.ValidationError("No email provided")
        if not data.get("content"):
            raise serializers.ValidationError("No content provided")

        return data

    def create(self, validated_data):
        return Contact.objects.create(**validated_data)
