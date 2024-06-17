from django.urls import path
from . import views
urlpatterns = [
    path('sessions/', views.show_sessions, name='sessions')
]
