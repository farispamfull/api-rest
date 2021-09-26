from rest_framework import viewsets

from .models import Lecture
from .serializers import LectureSerializer, LecturePostSerializer


class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return LectureSerializer
        return LecturePostSerializer
