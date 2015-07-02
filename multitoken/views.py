from rest_framework import permissions, generics, response, status
from . import serializers, utils


class LoginView(generics.GenericAPIView):
    """
    Use this endpoint to obtain user authentication token.
    """
    permission_classes = (
        permissions.AllowAny,
    )
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.DATA)
        if serializer.is_valid():
            return self.login(serializer)
        else:
            return response.Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def login(self, serializer):
        token = utils.get_or_create_token(user=serializer.user, serializer_data=serializer.data)
        return response.Response(
            data=serializers.TokenSerializer(token).data,
            status=status.HTTP_200_OK,
        )


class LogoutView(generics.GenericAPIView):
    """
    Use this endpoint to logout user (remove user authentication token).
    """
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def post(self, request):
        if request.auth:
            request.auth.delete()
        return response.Response(status=status.HTTP_200_OK)
