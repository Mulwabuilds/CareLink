from django.conf import settings

from django.db import models


class Notification(models.Model):

    class Type(models.TextChoices):

        APPOINTMENT = (
            "APPOINTMENT",
            "Appointment",
        )

        MESSAGE = (
            "MESSAGE",
            "Message",
        )

        HEALTH = (
            "HEALTH",
            "Health Update",
        )

        SYSTEM = (
            "SYSTEM",
            "System",
        )


    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications",
    )

    notification_type = models.CharField(
        max_length=20,
        choices=Type.choices,
        default=Type.SYSTEM,
    )

    title = models.CharField(
        max_length=150
    )

    message = models.TextField()

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:

        ordering = [
            "-created_at"
        ]