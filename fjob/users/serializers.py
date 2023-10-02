from django.contrib.auth import get_user_model, authenticate
from payment.models import UserPackage, Package
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db import transaction


UserModel = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

    @staticmethod
    def validate_email(email):
        if UserModel.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    @staticmethod
    def validate_username(username):
        if UserModel.objects.filter(username=username).exists():
            raise ValidationError("Username already exists")
        return username

    def create(self, validated_data):
        with transaction.atomic():
            user_obj = UserModel.objects.create_user(
                email=validated_data["email"],
                password=validated_data["password"],
                username=validated_data["username"],
            )
            package = Package.objects.get(id=1)
            #  Automatically add free trial package for a new user
            user_package = UserPackage(active=True, package=package, user=user_obj)
            user_package.save()

        return user_obj


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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("id", "email", "username")


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ChangeEmailSerializer(serializers.Serializer):
    old_email = serializers.EmailField(required=True)
    new_email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class AccountDeleteSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
