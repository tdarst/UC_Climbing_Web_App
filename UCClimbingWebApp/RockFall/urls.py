from django.urls import path
from . import views
urlpatterns = [
    path('rockfall/', views.rockfall, name='rockfall'),
    path('update_score/', views.update_score, name='update_score')
]