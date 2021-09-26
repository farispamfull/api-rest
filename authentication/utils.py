from django.conf import settings
from django.contrib.auth.tokens import default_token_generator,PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


class Util:
    @staticmethod
    def send_token_for_email(request, user):
        data = Util.token_generation_for_email(user)
        uid, token = data.values()
        current_site = get_current_site(request).domain
        relative_link = 'auth/activate-email'
        absurl = f'http://{current_site}/{relative_link}/{uid}/{token}'
        mail_subject = f'Verify your email from {current_site}'
        send_mail(mail_subject,
                  f'Your verify link: {absurl}',
                  f'{settings.EMAIL_FROM}@{current_site}',
                  [user.email],
                  fail_silently=False,
                  )

    @staticmethod
    def password_reset_token_created(request, user):
        current_site = get_current_site(request).domain
        token = PasswordResetTokenGenerator().make_token(user)
        absurl = f'{reverse("password_reset")}?token={token}'
        email_plaintext_message = (
            f'{user.username}, this is your password reset link\n'
            f'link: {absurl}')
        mail_subject = f'reset the password for the {current_site}'
        send_mail(mail_subject,
                  email_plaintext_message,
                  f'{settings.EMAIL_FROM}@{current_site}',
                  [user.email],
                  fail_silently=False,
                  )

    @staticmethod
    def token_generation_for_email(user):
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.id))
        return {'uid': uid, 'token': token, }
