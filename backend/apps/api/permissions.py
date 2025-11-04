from rest_framework import permissions

class RoleBasedAccessPermission(permissions.BasePermission):
    """
    Restricts access based on the logged-in user's role.
    """

    def has_permission(self, request, view):
        # Allow safe methods (GET, HEAD, OPTIONS) for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Must be authenticated for write operations
        if not request.user or not request.user.is_authenticated:
            return False

        # Example role logic (tweak as needed)
        if request.user.role == "Admin":
            return True
        if request.user.role == "HOD" and view.basename in ["departments", "timeslots"]:
            return True
        if request.user.role == "Faculty" and view.basename == "occupancies":
            return request.method in ["GET", "PUT"]
        if request.user.role == "Student":
            return request.method == "GET"

        return False
