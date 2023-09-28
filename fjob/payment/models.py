from django.db import models
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class Payment(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
