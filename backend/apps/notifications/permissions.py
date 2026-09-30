from rest_framework.permissions import BasePermission


class IsNotificationOwner(BasePermission):

    message = (
        "You can only access your own notifications."
    )

    def has_object_permission(
        self,
        request,
        view,
        obj,
    ):
        return obj.user == request.user