from rest_framework import permissions


class IsSuerUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
