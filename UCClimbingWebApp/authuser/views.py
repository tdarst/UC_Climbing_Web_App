from django.shortcuts import render, redirect
from .models import User, Profile
from .forms import ProfileUpdateForm
from login.forms import UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from login.views import activate_email

# View for user profile
@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    context = {
        'user': user
        
    }
    return render(request, 'login_templates/profile.html', context)

@login_required
def profile_update(request, username):
    view_msg = {
        "success" : "Profile has been updated sucessfully."
    }
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user, email_changed = user_form.save()
            profile_form.save()
            if email_changed:
                activate_email(request, user, user.cleaned_data.get('email'))
            messages.success(request, view_msg.get("success", settings.MESSAGE_RETRIEVAL_ERROR))
            return redirect('home')
        else:
            return redirect('home')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form' : user_form,
        'profile_form' : profile_form
    }
    return render(request, 'login_templates/update_profile.html', context)
