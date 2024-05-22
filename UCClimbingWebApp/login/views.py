from django.shortcuts import render

def login(request):
    return render(request, "login_templates/login.html")

def signup(request):
    return render(request, 'login_templates/signup.html')