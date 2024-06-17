import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include("home.urls")),
    path('', include("news.urls")),
    path('', include("login.urls")),
    path('', include("authuser.urls")),
    path('', include("RockFall.urls")),
    path('', include("sesh.urls")),
    path('admin/', admin.site.urls),
]

if os.environ.get('IS_ON_AWS', 0) != 1:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)