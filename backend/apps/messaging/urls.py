from django.urls import path

from .views import (
    MessageListCreateView,
    MessageDetailView,
)


urlpatterns = [
    path(
        "",
        MessageListCreateView.as_view(),
        name="message-list-create",
    ),
    path(
        "<int:pk>/",
        MessageDetailView.as_view(),
        name="message-detail",
    ),
]
