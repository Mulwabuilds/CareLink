from django.urls import path

from .views import (
    ProviderListView,
    MyProviderProfileView,
    PatientProviderCreateView,
    MyProviderRelationshipsView,
)


urlpatterns = [
    path(
        "",
        ProviderListView.as_view(),
        name="provider-list",
    ),

    path(
        "me/",
        MyProviderProfileView.as_view(),
        name="provider-me",
    ),

    path(
        "relationships/",
        MyProviderRelationshipsView.as_view(),
        name="provider-relationships",
    ),

    path(
        "relationships/create/",
        PatientProviderCreateView.as_view(),
        name="provider-relationship-create",
    ),
]