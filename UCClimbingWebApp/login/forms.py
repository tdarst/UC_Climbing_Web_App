from django import forms
from django.db import models

class UserCreationForm(models.Model):
    username = models.CharField(max_length=16)
    email = models.EmailField()
