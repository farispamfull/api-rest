from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken


class Util:
    @staticmethod
    def send_token_for_email(request, user):
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relative_link = reverse('email-verify')
        absurl = f'http://{current_site}{relative_link}?token={token}'
        mail_subject = f'Verify your email from {current_site}'
        email = user.email
        send_mail(mail_subject,
                  f'Your verify link: {absurl}',
                  f'{settings.EMAIL_FROM}@{current_site}',
                  [email],
                  fail_silently=False,
                  )
