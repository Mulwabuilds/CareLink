from django.utils import timezone

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Message
from .permissions import IsMessageParticipant
from .serializers import MessageSerializer


class MessageListCreateView(
    generics.ListCreateAPIView
):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        return Message.objects.filter(
            sender=user
        ) | Message.objects.filter(
            recipient=user
        )

    def perform_create(self, serializer):
        serializer.save(
            sender=self.request.user
        )


class MessageDetailView(
    generics.RetrieveUpdateAPIView
):
    serializer_class = MessageSerializer
    permission_classes = [
        IsAuthenticated,
        IsMessageParticipant,
    ]

    def get_queryset(self):
        user = self.request.user

        return Message.objects.filter(
            sender=user
        ) | Message.objects.filter(
            recipient=user
        )

    def perform_update(self, serializer):
        serializer.save(
            read_at=timezone.now()
        )
        