from django.db import models
from django.conf import settings
from datetime import date
from common import get_current_time
from django.template.defaultfilters import slugify

class ClimbingSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='climbing_session')
    date_posted = models.DateField(default=date.today)
    date_going = models.DateField(blank=False)
    time_going = models.TimeField(auto_now=False, auto_now_add=False, default=get_current_time)
    sesh_type = models.CharField(max_length=1000)
    sesh_environ = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000, default="Unspecified")
    
    joining = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='joining')
    maybe = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='maybe')
    
    slug = models.CharField(max_length=1000, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Session'
        verbose_name_plural = 'Sessions'

    def __str__(self):
        return f"{self.user}_{self.date_posted}_{self.sesh_type}"
    
    def save(self, *args, **kwargs):
        print(f"user - { self.user }")
        if not self.slug:
            self.slug = slugify(f"{self.user.username}-{self.date_posted}-{self.time_going}")
        return super().save(*args, **kwargs)
