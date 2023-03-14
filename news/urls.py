from django.urls import path
from .views import UserFinancialNewsView


urlpatterns = [
    path('user-financial-news/', UserFinancialNewsView.as_view())
]