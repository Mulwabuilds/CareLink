from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    class Role(models.TextChoices):

        PATIENT = (
            "PATIENT",
            "Patient",
        )

        PROVIDER = (
            "PROVIDER",
            "Healthcare Provider",
        )

        ADMIN = (
            "ADMIN",
            "Administrator",
        )


    email = models.EmailField(
        unique=True
    )


    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.PATIENT,
    )


    def __str__(self):
        return self.email