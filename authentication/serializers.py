from rest_framework import serializers

from user.models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'bio', 'age', 'gender')


class UserRegistrationSerializer(serializers.ModelSerializer):
    # profile = UserSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'username')
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     profile_data = validated_data.get('profile')
    #     if profile_data:
    #         validated_data.pop('profile')
    #         Profile.objects.create(**profile_data)
    #     user = User.objects.create(**profile_data)
    #     return user
