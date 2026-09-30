from django.urls import path

from .views import AdministrationStatusView


urlpatterns = [
    path(
        "status/",
        AdministrationStatusView.as_view(),
        name="administration-status",
    ),
]


