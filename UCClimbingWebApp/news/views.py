from django.shortcuts import render
from .models import Article


def news_article(request, slug_url):
    article = Article.objects.get(slug=slug_url)
    context = {
        'article':article,
        'slug':slug_url
    }
    return render(request, 'news_templates/article.html', context)

def news(request):
    all_articles = Article.objects.all().order_by('-date')
    context = {
        'articles':all_articles,
    }
    return render(request, "news_templates/news.html", context)