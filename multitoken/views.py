from django.contrib.auth.signals import user_logged_in
from rest_framework import permissions, generics, response, status
from . import serializers, utils


class ObtainTokenView(generics.GenericAPIView):
    """
    Use this endpoint to obtain user authentication token.
    """
    permission_classes = (
        permissions.AllowAny,
    )
    serializer_class = serializers.ObtainTokenSerializer
    token_serializer_class = serializers.TokenSerializer

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
        user_logged_in.send(sender=serializer.user.__class__, request=self.request, user=serializer.user)
        return response.Response(
            data=self.token_serializer_class(token).data,
            status=status.HTTP_200_OK,
        )


class InvalidateTokenView(generics.GenericAPIView):
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
