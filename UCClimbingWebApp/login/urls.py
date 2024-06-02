from django.urls import path
from . import views
urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_page, name="login"),
    path('signup/', views.signup, name="signup"),
    path('profile/<str:username>', views.profile, name='profile'),
    path('profile/<str:username>/password/', views.password_change, name='password'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]