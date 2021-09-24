from django.urls import path

from .views import UserRegistrationView, ActivateEmailView, UserLoginView, \
    ChangePasswordView

urlpatterns = [
    path('register/',
         UserRegistrationView.as_view(), name='register'),
    path('activate-email/<uidb64>/<token>/', ActivateEmailView.as_view(),
         name='activate_email'),
    path('signup/', UserLoginView.as_view()),
    path('change_password/', ChangePasswordView.as_view(),
         name='auth_change_password'),

]
