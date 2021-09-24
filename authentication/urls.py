from django.urls import path

from .views import UserRegistrationView, ActivateEmailView,UserLoginView

urlpatterns = [
    path('register/',
         UserRegistrationView.as_view(), name='register'),
    path('activate-email/<uidb64>/<token>/', ActivateEmailView.as_view(),
         name='activate_email'),
    path('signup/',UserLoginView.as_view())

]
