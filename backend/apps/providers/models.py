from django.conf import settings

from django.db import models


class ProviderProfile(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="provider_profile",
    )

    specialization = models.CharField(
        max_length=150
    )

    license_number = models.CharField(
        max_length=100,
        unique=True,
    )

    phone = models.CharField(
        max_length=30,
        blank=True,
    )

    is_available = models.BooleanField(
        default=True
    )


    def __str__(self):

        return (
            f"{self.user.get_full_name()} - "
            f"{self.specialization}"
        )


class PatientProvider(models.Model):

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="provider_relationships",
    )

    provider = models.ForeignKey(
        ProviderProfile,
        on_delete=models.CASCADE,
        related_name="patients",
    )

    active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:

        constraints = [

            models.UniqueConstraint(
                fields=[
                    "patient",
                    "provider",
                ],
                name="unique_patient_provider",
            )
        ]