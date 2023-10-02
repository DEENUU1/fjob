from rest_framework import permissions
from .models import UserPackage


class IsPackageAlreadyOwned(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        user = request.user
        package_id = view.kwargs.get("package_id")
        user_package = UserPackage.objects.filter(user=user, active=True).first()
        if user_package.package.id == package_id:
            return False
        return True
