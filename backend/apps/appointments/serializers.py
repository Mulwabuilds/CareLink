from rest_framework import serializers

from .models import Appointment


class AppointmentSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Appointment
        fields = [
            "id",
            "patient",
            "provider",
            "scheduled_for",
            "reason",
            "status",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "patient",
            "status",
            "created_at",
        ]

    def validate(self, attrs):
        request = self.context["request"]

        if request.user.role != "PATIENT":
            raise serializers.ValidationError(
                "Only patients can create appointments."
            )

        return attrs