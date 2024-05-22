from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("home.urls")),
    path('', include("news.urls")),
    path('', include("login.urls")),
    path('admin/', admin.site.urls),
]
