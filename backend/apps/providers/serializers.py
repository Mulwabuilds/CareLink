from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import ProviderProfile, PatientProvider


User = get_user_model()


class ProviderProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = ProviderProfile
        fields = [
            "id",
            "user",
            "specialization",
            "license_number",
            "phone",
            "is_available",
        ]
        read_only_fields = [
            "id",
            "user",
        ]


class PatientProviderSerializer(serializers.ModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    provider = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = PatientProvider
        fields = [
            "id",
            "patient",
            "provider",
            "active",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "patient",
            "provider",
            "created_at",
        ]