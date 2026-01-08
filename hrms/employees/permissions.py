from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsHRorAdminOrReadOnly(BasePermission):
    """
    HR and ADMIN can create/update/delete.
    EMPLOYEE can only read.
    """

    def has_permission(self, request, view):
        user = request.user

        # Must be logged in
        if not user or not user.is_authenticated:
            return False

        # Read-only access for all authenticated users
        if request.method in SAFE_METHODS:
            return True

        # Write access only for HR and ADMIN
        return user.role in ["HR", "ADMIN"]
