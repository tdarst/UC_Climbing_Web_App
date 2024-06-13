from django.urls import path
from . import views
urlpatterns = [
    path('rockfall/', views.rockfall, name='rockfall'),
]