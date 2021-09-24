from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from user.models import Profile, User


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Profile
        fields = ('user',
                  'first_name', 'last_name', 'bio', 'age', 'gender',
                  'birth_date',
                  'location')


class UserRegistrationSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'username', 'profile')
        extra_kwargs = {'password': {'write_only': True,
                                     'validators': [validate_password]}}

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        user = authenticate(password=password, email=email)
        if user is None:
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


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        validators=[validate_password],
        required=True)
    password2 = serializers.CharField(required=True)
    old_password = serializers.CharField(required=True)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return data
