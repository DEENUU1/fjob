from django.db.models.signals import post_save
from django.dispatch import receiver
from payment.models import UserPackage, Package
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_package(sender, instance, created, **kwargs):
    if created:
        package = Package.objects.get(id=1)
        UserPackage.objects.create(user=instance, active=True, package=package)
