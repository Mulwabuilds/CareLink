from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Appointment
from .permissions import IsAppointmentParticipant
from .serializers import AppointmentSerializer


class AppointmentListCreateView(
    generics.ListCreateAPIView
):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "PATIENT":
            return Appointment.objects.filter(
                patient=user
            )

        if user.role == "PROVIDER":
            return Appointment.objects.filter(
                provider=user
            )

        return Appointment.objects.all()

    def perform_create(self, serializer):
        serializer.save(
            patient=self.request.user
        )


class AppointmentDetailView(
    generics.RetrieveUpdateAPIView
):
    serializer_class = AppointmentSerializer
    permission_classes = [
        IsAuthenticated,
        IsAppointmentParticipant,
    ]

    def get_queryset(self):
        user = self.request.user

        if user.role == "PATIENT":
            return Appointment.objects.filter(
                patient=user
            )

        if user.role == "PROVIDER":
            return Appointment.objects.filter(
                provider=user
            )

        return Appointment.objects.all()

    def perform_update(self, serializer):
        serializer.save()