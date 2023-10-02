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
                if user_package.id in [2, 3]:
                    count_notifications = Notification.objects.filter(user=user).count()
                    if user_package.id == 2:
                        return count_notifications <= 3
                    if user_package.id == 3:
                        return count_notifications <= 5
            except UserPackage.DoesNotExist:
                return False
        return False
