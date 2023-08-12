from django.shortcuts import render
from .newsapi import get_news
from datetime import datetime

def index(request):
    topic = request.GET.get('topic')
    date_from_str = request.GET.get('date_from')
    date_to_str = request.GET.get('date_to')
    location = request.GET.get('location')
    date_from = datetime.strptime(date_from_str, '%Y-%m-%d') if date_from_str else None
    date_to = datetime.strptime(date_to_str, '%Y-%m-%d') if date_to_str else None



    if topic or date_from or date_to or location:
        articles = get_news(topic, date_from, date_to, location)
    else:
        articles = []

    return render(request, 'newsapp/index.html', {'articles': articles})
