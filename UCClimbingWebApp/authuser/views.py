from django.shortcuts import render
from .models import User, Profile

# View for user profile
def profile(request, username):
    user = User.objects.get(username=username)
    context = {
        'user': user
    }
    return render(request, 'login_templates/profile.html', context)

# View for user password change.
def password_change(request, username):
    return render(request, 'login_templates/password_change.html')
