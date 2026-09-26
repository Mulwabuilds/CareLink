from django.contrib.auth import get_user_model

from rest_framework import generics

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from .serializers import (
    RegisterSerializer,
    UserSerializer,
)


User = get_user_model()


class RegisterView(
    generics.CreateAPIView
):

    queryset = User.objects.all()

    serializer_class = RegisterSerializer

    permission_classes = [
        AllowAny
    ]


class MeView(
    generics.RetrieveUpdateAPIView
):

    serializer_class = UserSerializer

    permission_classes = [
        IsAuthenticated
    ]


    def get_object(self):

        return self.request.user