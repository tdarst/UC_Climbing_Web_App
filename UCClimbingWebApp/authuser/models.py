from __future__ import annotations
from django.contrib import admin
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.files.storage import default_storage as storage
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_stuff):
        if not username:
            raise ValueError("Please provide a valid username.")
        elif not email:
            raise ValueError("Please provide a valid email.")
        elif not password:
            raise ValueError("Pelase provide a valid password")
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_stuff)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)
    
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=16, blank=False, unique=True)
    email = models.EmailField(blank=True, default='', unique=True)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    FIRSTNAME_FIELD = "first_name"
    LASTNAME_FIELD = "last_name"
    REQUIRED_FIELDS = [EMAIL_FIELD, FIRSTNAME_FIELD, LASTNAME_FIELD]
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_short_name(self):
        return self.first_name or self.email.split('@')[0]
    
    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    score = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.user.username} Profile"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image_read = storage.open(self.image.name, "rb")
        img = Image.open(image_read)
        
        if img.height > 300 or self.image.width > 300:
            output_size = (300, 300)
            imageBuffer = BytesIO()
            img.thumbnail(output_size)
            
            img.save(imageBuffer, img.format)
            
            self.image.save(self.image.name, ContentFile(imageBuffer.getvalue()))