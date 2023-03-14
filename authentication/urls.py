from django.urls import path
from .views import UserRegistrationView, LoginView, LogoutView


urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', .as_view()),
]