from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import (UserRegistrationSerializer, UserLoginSerializer,
                          ChangePasswordSerializer, ResetPasswordSerializer,
                          ChangeResetPasswordSerializer)
from .utils import Util


class UserRegistrationView(APIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        Util.send_token_for_email(request, user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ActivateEmailView(APIView):

    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            if default_token_generator.check_token(user, token):
                user.is_verified = True
                user.save()
                return Response({'email': 'Successfully activated'},
                                status=status.HTTP_200_OK)
            return Response({'error': 'Invalid token'},
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as identifier:
            return Response({'error': 'Activation failed'},
                            status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ChangePasswordView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer
    model = User

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            if not object.check_password(
                    serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]},
                                status=status.HTTP_400_BAD_REQUEST)

            object.set_password(serializer.data.get("password"))
            object.save()
            response = {
                'username': object.username,
                'message': 'Password updated successfully',
            }

            return Response(response, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def password_reset(request):
    serializer = ChangeResetPasswordSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    user = User.objects.get(email=email)
    Util.password_reset_token_created(request, user)
    return Response({'status': 'OK'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def password_reset_confirm(request):
    serializer = ResetPasswordSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response({'status': 'OK'}, status=status.HTTP_200_OK)
