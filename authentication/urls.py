from django.urls import path
from .views import UserRegistrationView,VerifyEmail
urlpatterns = [
    path('register/',
         UserRegistrationView.as_view(), name='register'),
    path('email-verify/',VerifyEmail.as_view(),name='email-verify')

]
