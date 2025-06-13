from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user

class IsProprietario(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.groups.filter(name='Proprietario').exists()


class IsProprietarioOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return (
            request.user
            and request.user.is_authenticated
            and request.user.groups.filter(name="Proprietario").exists()
        )