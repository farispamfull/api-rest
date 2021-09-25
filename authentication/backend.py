from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import (InvalidToken,
                                                 AuthenticationFailed)
from rest_framework_simplejwt.settings import api_settings

User = get_user_model()


class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        """
        Attempts to find and return a user using the given validated token.
        """
        try:
            user_id = validated_token[api_settings.USER_ID_CLAIM]
        except KeyError:
            raise InvalidToken(
                _('Token contained no recognizable user identification'))

        try:
            user = self.user_model.objects.get(
                **{api_settings.USER_ID_FIELD: user_id})
        except self.user_model.DoesNotExist:
            raise AuthenticationFailed(_('User not found'),
                                       code='user_not_found')

        if not user.is_active:
            raise AuthenticationFailed(_('User is inactive'),
                                       code='user_inactive')
        if not user.is_verified:
            raise AuthenticationFailed(_("User is not verified."))

        return user


def custom_user_authentication_rule(user):
    return (
        True if user is not None and user.is_active and user.is_verified
        else False)


class AuthenticationBackend(BaseBackend):
    """
        Authentication Backend
        To manage the authentication process of user
    """

    def authenticate(self, request, email=None, password=None):
        try:
            user = User.objects.get(email=email, password=password)
        except User.DoesNotExist:
            return None
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
