from rest_framework import serializers

from .models import Lecture, User


class LecturePostSerializer(serializers.ModelSerializer):
    teacher = serializers.SlugRelatedField(slug_field='id',
                                           queryset=User.objects.all())

    class Meta:
        model = Lecture
        fields = ('id', 'title', 'teacher', 'description',
                  'lecturer_name', 'date', 'duration',
                  'slides_url', 'level', 'required')


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id', 'title', 'teacher', 'description',
                  'lecturer_name', 'date', 'duration',
                  'slides_url', 'level', 'required')
