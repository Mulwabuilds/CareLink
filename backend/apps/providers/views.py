from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import ProviderProfile, PatientProvider
from .permissions import (
    IsPatient,
    IsProvider,
    IsProviderOrAdmin,
)
from .serializers import (
    ProviderProfileSerializer,
    PatientProviderSerializer,
)


User = get_user_model()


class ProviderListView(generics.ListAPIView):
    queryset = ProviderProfile.objects.select_related("user")
    serializer_class = ProviderProfileSerializer
    permission_classes = [IsAuthenticated]


class MyProviderProfileView(
    generics.RetrieveUpdateAPIView
):
    serializer_class = ProviderProfileSerializer
    permission_classes = [IsProvider]

    def get_object(self):
        return ProviderProfile.objects.get(
            user=self.request.user
        )


class PatientProviderCreateView(
    generics.CreateAPIView
):
    serializer_class = PatientProviderSerializer
    permission_classes = [IsPatient]

    def perform_create(self, serializer):
        provider_id = self.request.data.get("provider")

        provider = ProviderProfile.objects.get(
            id=provider_id
        )

        serializer.save(
            patient=self.request.user,
            provider=provider,
        )


class MyProviderRelationshipsView(
    generics.ListAPIView
):
    serializer_class = PatientProviderSerializer

    def get_permissions(self):
        if self.request.user.role == "PROVIDER":
            return [IsProvider()]
        return [IsPatient()]

    def get_queryset(self):
        if self.request.user.role == "PROVIDER":
            return PatientProvider.objects.filter(
                provider__user=self.request.user
            )

        return PatientProvider.objects.filter(
            patient=self.request.user
        )