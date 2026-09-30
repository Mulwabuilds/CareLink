from rest_framework.permissions import BasePermission


class IsMessageParticipant(BasePermission):

    message = (
        "You can only access messages that you sent "
        "or received."
    )

    def has_object_permission(
        self,
        request,
        view,
        obj,
    ):
        return (
            obj.sender == request.user
            or obj.recipient == request.user
        )