from ..models import Contact
from rest_framework import serializers


class ContactUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ("read",)
