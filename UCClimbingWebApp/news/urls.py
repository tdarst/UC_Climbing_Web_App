from django.urls import path, include
from . import views
urlpatterns = [
    path('news/', views.news, name="news"),
    path('news/<str:slug>', views.news_article, name="news_article")
]
