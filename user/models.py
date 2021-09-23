from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
User = get_user_model()

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(
        max_length=50, blank=True, )
    last_name = models.CharField(
        max_length=50, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(blank=True,null=True)
    age = models.PositiveIntegerField(blank=True,null=True)

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
