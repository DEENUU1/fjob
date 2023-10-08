from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers


UserModel = get_user_model()


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid Credentials")

        data["user"] = user
        return data
