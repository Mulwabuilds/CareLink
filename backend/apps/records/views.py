from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import (
    MedicalRecord,
    HealthUpdate,
    RecoveryUpdate,
)

from .permissions import (
    IsPatient,
    IsProvider,
)

from .serializers import (
    MedicalRecordSerializer,
    HealthUpdateSerializer,
    RecoveryUpdateSerializer,
)


class MedicalRecordListCreateView(
    generics.ListCreateAPIView
):
    serializer_class = MedicalRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "PROVIDER":
            return MedicalRecord.objects.filter(
                provider=user
            )

        if user.role == "PATIENT":
            return MedicalRecord.objects.filter(
                patient=user
            )

        return MedicalRecord.objects.all()

    def perform_create(self, serializer):
        serializer.save(
            provider=self.request.user
        )


class MedicalRecordDetailView(
    generics.RetrieveUpdateAPIView
):
    serializer_class = MedicalRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "PROVIDER":
            return MedicalRecord.objects.filter(
                provider=user
            )

        if user.role == "PATIENT":
            return MedicalRecord.objects.filter(
                patient=user
            )

        return MedicalRecord.objects.all()


class HealthUpdateListCreateView(
    generics.ListCreateAPIView
):
    serializer_class = HealthUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "PATIENT":
            return HealthUpdate.objects.filter(
                patient=user
            )

        return HealthUpdate.objects.all()

    def perform_create(self, serializer):
        serializer.save(
            patient=self.request.user
        )


class HealthUpdateDetailView(
    generics.RetrieveAPIView
):
    serializer_class = HealthUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "PATIENT":
            return HealthUpdate.objects.filter(
                patient=user
            )

        return HealthUpdate.objects.all()


class RecoveryUpdateListCreateView(
    generics.ListCreateAPIView
):
    serializer_class = RecoveryUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "PATIENT":
            return RecoveryUpdate.objects.filter(
                patient=user
            )

        return RecoveryUpdate.objects.all()

    def perform_create(self, serializer):
        serializer.save(
            patient=self.request.user
        )


class RecoveryUpdateDetailView(
    generics.RetrieveAPIView
):
    serializer_class = RecoveryUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "PATIENT":
            return RecoveryUpdate.objects.filter(
                patient=user
            )

        return RecoveryUpdate.objects.all()