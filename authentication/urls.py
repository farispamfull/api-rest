from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (UserRegistrationView, ActivateEmailView, UserLoginView,
                    ChangePasswordView, password_reset, password_reset_confirm)

urlpatterns = [
    path('register/',
         UserRegistrationView.as_view(), name='register'),
    path('activate-email/<uidb64>/<token>/', ActivateEmailView.as_view(),
         name='activate_email'),
    path('signup/', UserLoginView.as_view(),name='signup'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_password/', ChangePasswordView.as_view(),
         name='change_password'),
    path('password_reset/', password_reset, name='password_reset'),
    path('password_reset/confirm/', password_reset_confirm,
         name='password_res_confirm')
]
