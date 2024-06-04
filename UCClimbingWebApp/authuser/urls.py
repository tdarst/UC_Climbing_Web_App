from django.urls import path
from . import views
urlpatterns = [
    path('profile/<str:username>', views.profile, name='profile'),
    path('profile/<str:username>/password/', views.password_change, name='password')
]