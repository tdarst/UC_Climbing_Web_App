from django.shortcuts import render, redirect

def show_sessions(request):
    return redirect(request, 'sesh_templates/sesh_template.html')
