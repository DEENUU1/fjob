from django.core.management.base import BaseCommand
from payment.models import Package


class Command(BaseCommand):
    help = "Create default Package objects"

    def handle(self, *args, **kwargs):
        print("działa")
        package_1 = Package.objects.create(
            name="Free",
        )
        package_2 = Package.objects.create(
            name="Basic",
            price=100,
            is_free=False,
        )
        package_3 = Package.objects.create(
            name="Advanced",
            price=500,
            has_signals=True,
            is_free=False,
        )

        package_1.save()
        package_2.save()
        package_3.save()
