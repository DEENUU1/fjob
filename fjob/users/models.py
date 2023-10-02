from django.contrib.auth.models import (
    AbstractBaseUser,
    Permission,
    PermissionsMixin,
    Group,
)
from django.db import models


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
