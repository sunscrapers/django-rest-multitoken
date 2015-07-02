from . import models


def get_or_create_token(user, serializer_data=None):
    serializer_data = serializer_data or {}
    token_data = dict((k, v) for k, v in serializer_data.items() if k in models.Token.LOGIN_FIELDS)
    token, _ = models.Token.objects.get_or_create(user=user, **token_data)
    return token
