from django.shortcuts import render
from django.db.models import Q
from .models import NewsArticle

def news_list(request):
    query = request.GET.get('q')
    articles = NewsArticle.objects.all()

    if query:
        articles = articles.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    # You can add more filter logic here for Topic, Date, Location
    
    return render(request, 'newsapp/news_list.html', {'articles': articles})
