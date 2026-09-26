from django.conf import settings

from django.db import models


class Appointment(models.Model):

    class Status(models.TextChoices):

        PENDING = (
            "PENDING",
            "Pending",
        )

        CONFIRMED = (
            "CONFIRMED",
            "Confirmed",
        )

        COMPLETED = (
            "COMPLETED",
            "Completed",
        )

        CANCELLED = (
            "CANCELLED",
            "Cancelled",
        )


    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="patient_appointments",
    )

    provider = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="provider_appointments",
    )

    scheduled_for = models.DateTimeField()

    reason = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:

        ordering = [
            "scheduled_for"
        ]