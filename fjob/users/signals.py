from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from payment.models import UserPackage


@receiver(post_save, sender=CustomUser)
def user_package_created(sender, instance, created, **kwargs):
    if created:
        user_package = UserPackage(user=instance, package=1, active=True)
        user_package.save()
