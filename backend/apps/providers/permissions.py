from rest_framework.permissions import BasePermission


class IsProvider(BasePermission):
    message = "Only healthcare providers can perform this action."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "PROVIDER"
        )


class IsPatient(BasePermission):
    message = "Only patients can perform this action."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "PATIENT"
        )


class IsProviderOrAdmin(BasePermission):
    message = "Only providers or administrators can perform this action."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in ["PROVIDER", "ADMIN"]
        )