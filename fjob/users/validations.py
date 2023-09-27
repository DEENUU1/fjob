from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


UserModel = get_user_model()


def custom_validation(data):
    email = data["email"].strip()
    first_name = data["first_name"].strip()
    last_name = data["last_name"].strip()
    password = data["password"].strip()

    if not email or UserModel.objects.filter(email=email).exists():
        raise ValidationError("Email already exists")

    if not password or len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long")

    if not first_name or last_name:
        raise ValidationError("First and last name are required")
    return data


def validate_email(data):
    email = data["email"].strip()
    if not email:
        raise ValidationError("Email is required")
    return True


def validate_password(data):
    password = data["password"].strip()
    if not password:
        raise ValidationError("Password is required")
    return True
