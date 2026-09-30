from rest_framework import serializers

from .models import Message


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = [
            "id",
            "sender",
            "recipient",
            "content",
            "sent_at",
            "read_at",
        ]

        read_only_fields = [
            "id",
            "sender",
            "sent_at",
            "read_at",
        ]

    def validate_recipient(self, value):
        request = self.context["request"]

        if value == request.user:
            raise serializers.ValidationError(
                "You cannot send a message to yourself."
            )

        return value