from django.conf import settings

from django.db import models


class Message(models.Model):

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_messages",
    )

    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="received_messages",
    )

    content = models.TextField()

    sent_at = models.DateTimeField(
        auto_now_add=True
    )

    read_at = models.DateTimeField(
        null=True,
        blank=True,
    )


    class Meta:

        ordering = [
            "sent_at"
        ]