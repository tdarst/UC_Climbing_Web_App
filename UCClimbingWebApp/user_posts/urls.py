from django.urls import path
from . import views
urlpatterns = [
    path('sessions/', views.sessions_view, name="sessions"),
    path('joining/<str:slug_url>', views.joining_session, name="joining"),
]
