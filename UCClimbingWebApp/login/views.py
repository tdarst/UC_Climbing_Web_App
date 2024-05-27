from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from authuser.models import User
from .forms import CustomUserCreationForm, UserLoginForm
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
        
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        
        messages.success(request, "Account activated! Thank you for your email confirmation.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid.")
        
    return redirect('home')

def activateEmail(request, user, to_email):
    mail_subject = "Activate your climbing team account"
    message = render_to_string("email/activate_account_template.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f"Account creation success! Please check your email for activation link.")
        
    else:
        messages.error(request, "Problem sending email")

def login_page(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.authenticate_user()
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            form.add_error(None,'Invalid username or password.')
            
        return render(request, "login_templates/login.html")
    
    else:
        form = UserLoginForm()
    return render(request, "login_templates/login.html", {'form' : form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'login_templates/signup.html', {'form':form})

def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'login_templates/profile.html', {'user': user})