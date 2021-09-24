from django.urls import path

from .views import UserRegistrationView, ActivateEmailView, UserLoginView, \
    ChangePasswordView, password_reset, password_reset_confirm

urlpatterns = [
    path('register/',
         UserRegistrationView.as_view(), name='register'),
    path('activate-email/<uidb64>/<token>/', ActivateEmailView.as_view(),
         name='activate_email'),
    path('signup/', UserLoginView.as_view()),
    path('change_password/', ChangePasswordView.as_view(),
         name='auth_change_password'),
    path('password_reset/', password_reset, name='password_reset'),
    path('password_reset/confirm/', password_reset_confirm)
]
