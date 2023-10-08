from django.contrib.auth import get_user_model
from rest_framework import serializers


UserModel = get_user_model()


class AccountDeleteSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
