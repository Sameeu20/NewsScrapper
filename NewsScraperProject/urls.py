from django.urls import path
from newsapp.views import news_list

urlpatterns = [
    path('news/', news_list, name='news-list'),
    # Add other URLs as needed
]
