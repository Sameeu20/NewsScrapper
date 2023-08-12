import requests
from datetime import datetime

NEWS_API_KEY = 'c3d9a3e8fc754f4dae1d0045541ecfe0'

def get_news(topic, date_from=None, date_to=None, location=None):
    base_url = 'https://newsapi.org/v2/everything'

    params = {
        'q': topic,
        'apiKey': NEWS_API_KEY,
    }

    if date_from:
        params['from'] = date_from.strftime('%Y-%m-%d')
    if date_to:
        params['to'] = date_to.strftime('%Y-%m-%d')
    if location:
        params['location'] = location

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get('articles', [])
        print(articles)  # Debug: Print the retrieved articles
    else:
        return []
