from django.db import models
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class Package(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    has_signals = models.BooleanField(default=False)
    num_of_signals = models.IntegerField(default=0)
    is_free = models.BooleanField(default=True)
    free_users = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def cents_to_dollar(self):
        if self.price == 0:
            return 0
        else:
            return self.price / 100

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Packages"
        verbose_name = "Package"

    def __str__(self):
        return f"{self.name} - {self.price}$"


class UserPackage(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(
        max_length=500, blank=True, null=True, default=None
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "User Packages"
        verbose_name = "User Package"

    def __str__(self):
        return f"{self.user} - {self.package}"
