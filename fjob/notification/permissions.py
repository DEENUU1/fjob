from rest_framework import permissions
from payment.models import UserPackage


class CanAccessNotification(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        user = request.user
        if user.is_authenticated:
            try:
                user_package = UserPackage.objects.get(user=user, active=True).first()
                return user_package.id in [2, 3]
            except UserPackage.DoesNotExist:
                return False
        return False
