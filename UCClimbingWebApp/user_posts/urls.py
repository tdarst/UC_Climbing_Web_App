from django.urls import path
from . import views
urlpatterns = [
    path('sessions/', views.sessions_view, name="sessions"),
    path('post_sesh/', views.post_session, name="post_sesh"),
    path('post_sesh/post/', views.post_session, name="post_sesh_post"),
    path('joining/<str:slug_url>/', views.joining_session, name="joining"),
]
