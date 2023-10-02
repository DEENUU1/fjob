from rest_framework import permissions
from payment.models import UserPackage
from .models import Notification


class CanAccessNotification(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        user = request.user
        if user.is_authenticated:
            try:
                user_package = UserPackage.objects.filter(
                    user=user, active=True
                ).first()
                if user_package.package.has_signals:
                    user_package_count = Notification.objects.filter(user=user).count()
                    if user_package_count < user_package.package.num_of_signals:
                        return True
                    else:
                        return False
                else:
                    return False
            except UserPackage.DoesNotExist:
                return False
        return False
