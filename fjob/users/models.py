from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    Permission,
    PermissionsMixin,
    Group,
)
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, username=None):
        if not email:
            raise ValueError("An email address is required")
        if not password:
            raise ValueError("A password is required")
        if not username:
            raise ValueError("A  username is required")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, username=None):
        if not email:
            raise ValueError("An email address is required")
        if not password:
            raise ValueError("A password is required")
        if not username:
            raise ValueError("A  username is required")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    groups = models.ManyToManyField(Group, blank=True, related_name="customuser_set")
    user_permissions = models.ManyToManyField(
        Permission, blank=True, related_name="customuser_set"
    )

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"

    def __str__(self):
        return self.email
