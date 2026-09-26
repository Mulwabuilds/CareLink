from django.conf import settings

from django.db import models


class MedicalRecord(models.Model):

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="medical_records",
    )

    provider = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="created_medical_records",
    )

    diagnosis = models.CharField(
        max_length=255
    )

    notes = models.TextField()

    treatment = models.TextField(
        blank=True
    )

    recorded_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


    class Meta:

        ordering = [
            "-recorded_at"
        ]


class HealthUpdate(models.Model):

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="health_updates",
    )

    symptoms = models.TextField(
        blank=True
    )

    temperature = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True,
    )

    blood_pressure = models.CharField(
        max_length=20,
        blank=True,
    )

    heart_rate = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:

        ordering = [
            "-created_at"
        ]


class RecoveryUpdate(models.Model):

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recovery_updates",
    )

    progress = models.PositiveSmallIntegerField(
        help_text="Progress percentage from 0 to 100."
    )

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:

        ordering = [
            "-created_at"
        ]