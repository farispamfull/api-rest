from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserRegistrationSerializer, UserLoginSerializer
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
    # permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
