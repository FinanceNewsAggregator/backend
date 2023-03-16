from django.urls import path
from .views import UserFinancialNewsView


urlpatterns = [
    path('user-news/', UserFinancialNewsView.as_view())
]