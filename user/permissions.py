from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user

class IsUserReadOnly(BasePermission):
    def has_permissions(self, request, view):
        if request.method in SAFE_METHODS:
            return (
                request.user
                and request.user.is_authenticated
                and request.user.groups.filter(name='Usuario').exists()
            )
        return False




