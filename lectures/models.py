from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Lecture(models.Model):

    teacher = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    lecturer_name = models.CharField(max_length=100, default='',
                                     blank=True)
    date = models.DateField()
    duration = models.IntegerField(help_text='Enter number of hours')
    slides_url = models.CharField(max_length=255)
    level = models.IntegerField(choices=((1, 'Level 1'), (2, 'Level 2')),
                                default=1)
    required = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Attendance(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
