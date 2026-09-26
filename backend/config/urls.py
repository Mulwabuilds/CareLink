from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [

    # Django administration
    path(
        "admin/",
        admin.site.urls,
    ),

    # Authentication
    path(
        "api/auth/refresh/",
        TokenRefreshView.as_view(),
        name="token-refresh",
    ),

    # CareLink applications
    path(
        "api/accounts/",
        include("apps.accounts.urls"),
    ),

    path(
        "api/providers/",
        include("apps.providers.urls"),
    ),

    path(
        "api/records/",
        include("apps.records.urls"),
    ),

    path(
        "api/appointments/",
        include("apps.appointments.urls"),
    ),

    path(
        "api/messaging/",
        include("apps.messaging.urls"),
    ),

    path(
        "api/notifications/",
        include("apps.notifications.urls"),
    ),

    path(
        "api/administration/",
        include("apps.administration.urls"),
    ),
]