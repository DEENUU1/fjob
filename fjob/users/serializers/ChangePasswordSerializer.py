from django.contrib.auth import get_user_model
from rest_framework import serializers


UserModel = get_user_model()


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context.get("request").user
        if not user.check_password(value):
            raise serializers.ValidationError("Incorrect old password.")
        return value

    def update_password(self, user):
        new_password = self.validated_data["new_password"]
        user.set_password(new_password)
        user.save()
