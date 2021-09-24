from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from user.models import Profile, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'first_name', 'last_name', 'bio', 'age', 'gender', 'birth_date',
            'location')


class UserRegistrationSerializer(serializers.ModelSerializer):
    profile = UserSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'username', 'profile')
        extra_kwargs = {'password': {'write_only': True,
                                     'validators': [validate_password]}}


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        user = authenticate(password='AniDUBRu1818',email='dasha@gmail.com')
        print(user,password,email)
        print(user.check_password(password))
        if user is None:
            print(user==None,user is None)
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        if not user.is_verified:
            raise serializers.ValidationError('Email is not verified')
        if not user.is_active:
            raise serializers.ValidationError(
                'Account disabled, contact admin')

        return {
            'email': user.email,
            'token': user.token()
        }
