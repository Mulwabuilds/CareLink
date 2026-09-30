from django.urls import path

from .views import (
    MedicalRecordListCreateView,
    MedicalRecordDetailView,
    HealthUpdateListCreateView,
    HealthUpdateDetailView,
    RecoveryUpdateListCreateView,
    RecoveryUpdateDetailView,
)


urlpatterns = [
    path(
        "medical/",
        MedicalRecordListCreateView.as_view(),
        name="medical-record-list-create",
    ),

    path(
        "medical/<int:pk>/",
        MedicalRecordDetailView.as_view(),
        name="medical-record-detail",
    ),

    path(
        "health/",
        HealthUpdateListCreateView.as_view(),
        name="health-update-list-create",
    ),

    path(
        "health/<int:pk>/",
        HealthUpdateDetailView.as_view(),
        name="health-update-detail",
    ),

    path(
        "recovery/",
        RecoveryUpdateListCreateView.as_view(),
        name="recovery-update-list-create",
    ),

    path(
        "recovery/<int:pk>/",
        RecoveryUpdateDetailView.as_view(),
        name="recovery-update-detail",
    ),
]