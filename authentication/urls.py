from django.urls import path
from .views import UserRegistrationView, LoginView, LogoutView


urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view())
]