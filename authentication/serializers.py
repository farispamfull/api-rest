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

    # def create(self, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     user = User.objects.create(**validated_data)
    #     if profile_data:
    #         print('fggggggggggg')
    #         profile = Profile(**profile_data)
    #         profile.user = user
    #         profile.save()
    #
    #     return user
    #
    #     # profile_data = validated_data.get('profile')
    #     # if profile_data:
    #     #     validated_data.pop('profile')
    #     # Profile.objects.create(**profile_data)
    #     # return User.objects.create(**validated_data)
