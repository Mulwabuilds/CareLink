from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class AdministrationStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != "ADMIN":
            return Response(
                {
                    "detail": (
                        "Administrator access required."
                    )
                },
                status=403,
            )

        return Response(
            {
                "status": "Administration API available.",
                "user": request.user.email,
            }
        )