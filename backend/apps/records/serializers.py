from rest_framework import serializers

from .models import (
    MedicalRecord,
    HealthUpdate,
    RecoveryUpdate,
)


class MedicalRecordSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = MedicalRecord
        fields = [
            "id",
            "patient",
            "provider",
            "diagnosis",
            "notes",
            "treatment",
            "recorded_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "provider",
            "recorded_at",
            "updated_at",
        ]


class HealthUpdateSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = HealthUpdate
        fields = [
            "id",
            "patient",
            "symptoms",
            "temperature",
            "blood_pressure",
            "heart_rate",
            "notes",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "patient",
            "created_at",
        ]


class RecoveryUpdateSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = RecoveryUpdate
        fields = [
            "id",
            "patient",
            "progress",
            "notes",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "patient",
            "created_at",
        ]

    def validate_progress(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError(
                "Progress must be between 0 and 100."
            )

        return value