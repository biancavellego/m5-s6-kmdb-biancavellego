from rest_framework import permissions
from rest_framework.views import View

class IsAdminOrCreate(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return (
            request.method == "GET"
            and request.user.is_authenticated
            and request.user.is_superuser
            or request.method == "POST"
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return (
            request.method in permissions.SAFE_METHODS or
            request.user.is_authenticated
            and request.user.is_superuser
        )

class IsAdminOrCriticOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return (
            request.method in permissions.SAFE_METHODS or
            request.user.is_authenticated and request.user.is_superuser 
            or request.user.is_authenticated and request.user.is_critic
        )
