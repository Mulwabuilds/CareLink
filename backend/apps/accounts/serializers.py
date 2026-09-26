from django.contrib.auth import get_user_model

from rest_framework import serializers


User = get_user_model()


class UserSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = User

        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "role",
        ]

        read_only_fields = [
            "id",
            "role",
        ]


class RegisterSerializer(
    serializers.ModelSerializer
):

    password = serializers.CharField(
        write_only=True,
        min_length=8,
    )


    class Meta:

        model = User

        fields = [
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "role",
        ]


    def create(
        self,
        validated_data
    ):

        return User.objects.create_user(
            **validated_data
        )