from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit/delete it.
    Read operations (GET, HEAD, OPTIONS) are allowed to any authenticated user.
    Write operations (POST, PUT, PATCH, DELETE) are only allowed to the owner.
    """

    def has_permission(self, request, view):
        # Require authentication for all operations
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow read permissions to any authenticated user
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner
        # Check if the object has an 'owner' field pointing to Account
        if hasattr(obj, 'owner'):
            return obj.owner == request.user

        # Check for 'account' field (used by Ticket)
        if hasattr(obj, 'account'):
            return obj.account == request.user

        # Check for 'vessel' field (used by Passage - check vessel owner)
        if hasattr(obj, 'vessel'):
            vessel_owner = obj.vessel.owner
            return vessel_owner == request.user

        return False


class IsOwnerOnly(permissions.BasePermission):
    """
    Custom permission to restrict ALL access (read and write) to the owner only.
    Only the owner of the object can view, create, edit, or delete it.
    Used for sensitive data like Passage where users should only see their own records.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the object has an 'owner' field pointing to Account
        if hasattr(obj, 'owner'):
            return obj.owner == request.user

        # Check for 'account' field (used by Ticket)
        if hasattr(obj, 'account'):
            return obj.account == request.user

        # Check for 'vessel' field (used by Passage - check vessel owner)
        if hasattr(obj, 'vessel'):
            vessel_owner = obj.vessel.owner
            return vessel_owner == request.user

        return False

    def has_permission(self, request, view):
        # Require authentication for all operations
        return request.user and request.user.is_authenticated
