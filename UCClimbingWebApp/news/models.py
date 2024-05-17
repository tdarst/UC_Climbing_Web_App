from django.db import models
from datetime import date
from authuser.models import User
from django.template.defaultfilters import slugify

class Article(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    contents = models.TextField(help_text="Write content here.", default='')
    date = models.DateField(default=date.today)
    slug = models.CharField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return f"Title: {self.title}, Author: {str(self.author)}, Date: {self.date}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{str(self.author)}-{self.date}")
        return super().save(*args, **kwargs)
    
    