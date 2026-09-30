from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Notification
from .permissions import IsNotificationOwner
from .serializers import NotificationSerializer


class NotificationListView(
    generics.ListAPIView
):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(
            user=self.request.user
        )


class NotificationDetailView(
    generics.RetrieveUpdateAPIView
):
    serializer_class = NotificationSerializer
    permission_classes = [
        IsAuthenticated,
        IsNotificationOwner,
    ]

    def get_queryset(self):
        return Notification.objects.filter(
            user=self.request.user
        )