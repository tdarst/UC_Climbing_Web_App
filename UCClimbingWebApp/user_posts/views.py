from django.shortcuts import render, redirect
from .models import ClimbingSession
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.db.models import Count
from .forms import ClimbingSessionForm
from django.contrib.auth.decorators import login_required

def sessions_view(request):
    sessions = ClimbingSession.objects.all().annotate(
        joining_count=Count('joining')
    )
    context = {
        "sessions" : sessions
    }
    return render(request, "sesh_templates/sesh_template.html", context)

def post_session(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ClimbingSessionForm(request.POST)
            if form.is_valid():
                sesh = form.save(commit=False)
                sesh.user = request.user
                sesh.save()
        else:
            form = ClimbingSessionForm()
        context = {
            "form" : form
        }

        return render(request, 'sesh_templates/create_session.html', context)
    else:
        return redirect('login')

def joining_session(request, slug_url):
    user = request.user
    if user.is_authenticated:
        msg = {
            'success' : lambda user_first_name: f"Successfully joined {user_first_name}'s session.",
            'error' : lambda user_first_name: f"Error: Could not join {user_first_name}'s session"
        }
        climbing_session = ClimbingSession.objects.get(slug=slug_url)
        
        user.joining.add(climbing_session)
        user.save()
        
        climbing_session.joining.add(user)
        climbing_session.save()
        
        if user.joining.filter(slug=climbing_session.slug).exists():
            messages.success(request, msg.get('success', settings.MESSAGE_RETRIEVAL_ERROR)(climbing_session.user.first_name))
        else:
            messages.error(request, msg.get('error', settings.MESSAGE_RETRIEVAL_ERROR)(climbing_session.user.first_name))
            
        return redirect("sessions")
    
    else:
        return redirect('login')