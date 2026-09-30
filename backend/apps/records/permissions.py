from rest_framework.permissions import BasePermission


class IsPatient(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "PATIENT"
        )


class IsProvider(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "PROVIDER"
        )