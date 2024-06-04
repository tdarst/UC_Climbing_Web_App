from django.urls import path
from . import views
urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_page, name="login"),
    path('signup/', views.signup, name="signup"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]