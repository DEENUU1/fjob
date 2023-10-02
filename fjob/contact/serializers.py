from rest_framework.serializers import Serializer
from .models import Contact


class ContactSerializer(Serializer):
    class Meta:
        fields = '__all__'
        model = Contact
