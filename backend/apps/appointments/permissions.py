from rest_framework.permissions import BasePermission


class IsAppointmentParticipant(
    BasePermission
):

    def has_object_permission(
        self,
        request,
        view,
        obj,
    ):
        return (
            obj.patient == request.user
            or obj.provider == request.user
            or request.user.role == "ADMIN"
        )