from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.exceptions import ValidationError
from payment.models import UserPackage, Package

UserModel = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

    def create(self, validated_data):
        user_obj = UserModel.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            username=validated_data["username"],
        )
        package = Package.objects.get(id=1)
        user_package = UserPackage(active=True, package=package, user=user_obj)
        user_package.save()

        user_obj.save()
        return user_obj


class UserPasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField()
    new_password = serializers.CharField()

    def update(self, instance, validated_data):
        current_password = validated_data.get("current_password")
        new_password = validated_data.get("new_password")

        if not instance.check_password(current_password):
            raise ValidationError("Current password is incorrect")

        instance.set_password(new_password)
        instance.save()
        return instance


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def check_user(self, validated_data):
        user = authenticate(
            username=validated_data["username"], password=validated_data["password"]
        )
        if not user:
            raise ValidationError("Invalid credentials")
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("id", "email", "username")
