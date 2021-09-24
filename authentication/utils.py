from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

class Util:
    @staticmethod
    def send_token_for_email(request, user):
        token = default_token_generator.make_token(user)
        uid=urlsafe_base64_encode(force_bytes(user.id))
        current_site = get_current_site(request).domain
        relative_link = 'activate-email'
        absurl = f'http://{current_site}/{relative_link}/{uid}/{token}'
        mail_subject = f'Verify your email from {current_site}'
        email = user.email
        send_mail(mail_subject,
                  f'Your verify link: {absurl}',
                  f'{settings.EMAIL_FROM}@{current_site}',
                  [email],
                  fail_silently=False,
                  )
