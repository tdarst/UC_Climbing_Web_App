from django.shortcuts import render, redirect
from .models import ClimbingSession
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse

def sessions_view(request):
    sessions = ClimbingSession.objects.all()
    context = {
        "sessions" : sessions
    }
    return render(request, "sesh_templates/sesh_template.html", context)

def joining_session(request, slug_url):
    msg = {
        'success' : lambda user_first_name: f"Successfully joined {user_first_name}'s session.",
        'error' : lambda user_first_name: f"Error: Could not join {user_first_name}'s session"
    }
    user = request.user
    climbing_session = ClimbingSession.objects.get(slug=slug_url)
    
    user.joining.add(climbing_session)
    user.save()
    
    climbing_session.joining.add(user)
    climbing_session.save()
    
    if user.joining.filter(slug=climbing_session.slug).exists():
        messages.success(request, msg.get('success', settings.MESSAGE_RETRIEVAL_ERROR)(user.first_name))
        http_status = 200
        return HttpResponse(status=http_status)
        
    else:
        messages.error(request, msg.get('error', settings.MESSAGE_RETRIEVAL_ERROR)(user.first_name))
        return redirect('sessions')