from rest_framework import generics,status
from .serializers import UserRegistrationSerializer
from rest_framework.response import Response


class UserRegistrationView(generics.GenericAPIView):
    serializer_class = UserRegistrationSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
