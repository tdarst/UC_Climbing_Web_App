from django import forms
from authuser.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.conf import settings

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=16)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=16)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email']
        
    def save(self, commit=True, email_changed=False):
        user = super().save(commit=False)
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if email_changed:
            user.is_active = False
        if commit:
            user.save()
            
        return user, email_changed
        
        
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=16)
    password = forms.CharField(widget=forms.PasswordInput, max_length=150)
    
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def authenticate_user(self):
        user = self.cleaned_data['username']
        passw = self.cleaned_data['password']
        if user and passw:
            user = authenticate(username=user, password=passw)
        return user