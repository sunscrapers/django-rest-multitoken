from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from . import models, constants

User = get_user_model()


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = models.Token
        fields = (
            'auth_token',
        )


class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(required=False)
    client = serializers.CharField()

    default_error_messages = {
        'inactive_account': constants.INACTIVE_ACCOUNT_ERROR,
        'invalid_credentials': constants.INVALID_CREDENTIALS_ERROR,
    }

    def __init__(self, *args, **kwargs):
        super(LoginSerializer, self).__init__(*args, **kwargs)
        self.user = None
        self.fields[User.USERNAME_FIELD] = serializers.CharField(required=False)

    def validate(self, attrs):
        self.user = authenticate(username=attrs[User.USERNAME_FIELD], password=attrs['password'])
        if self.user:
            if not self.user.is_active:
                raise serializers.ValidationError(self.error_messages['inactive_account'])
            return attrs
        else:
            raise serializers.ValidationError(self.error_messages['invalid_credentials'])
