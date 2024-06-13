from django.urls import path
from . import views
urlpatterns = [
    path('profile/<str:username>', views.profile, name='profile'),
    path('profile/<str:username>/update/', views.profile_update, name='update_profile')
]