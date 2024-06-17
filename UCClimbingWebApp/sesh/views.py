from django.shortcuts import render
from .models import sesh

def show_sessions(request):
    sessions = sesh.objects.get()
    context = {
        "sessions" : sessions
    }
    return render(request, 'sesh_templates/sesh_template.html', context)
