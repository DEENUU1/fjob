from django.contrib.auth import get_user_model
from payment.models import Package, UserPackage

UserModel = get_user_model()


# def update_free_uses(user):
#     user_package = UserPackage.objects.filter(user=user, active=True).first()
#     if user_package.package == 1:
