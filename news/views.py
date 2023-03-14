import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from django.contrib.auth import get_user_model


User = get_user_model()


# News API client library to fetch news based on the user's selected sources
class UserFinancialNewsView(APIView):
    def get(self, request):
        user = request.user
        sources = user.tags.split(',')
        news_api_url = f'https://newsapi.org/v2/top-headlines?sources={",".join(sources)}&category=business&apiKey={settings.NEWS_API_KEY}'
        response = requests.get(news_api_url)
        data = response.json()
        return Response(data)