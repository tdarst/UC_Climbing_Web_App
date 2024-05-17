from django.shortcuts import render
from .models import Article

def news(request):
    all_articles = Article.objects.all()
    context = {
        'articles':all_articles
    }
    return render(request, "news_templates/news.html", context)