from rest_framework import authentication
from . import models


class TokenAuthentication(authentication.TokenAuthentication):
    model = models.Token
