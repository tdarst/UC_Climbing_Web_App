from django.db import models
from django.conf import settings
from datetime import date

class sesh(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sesh')
    date_posted = models.DateField(default=date.today)
    date_going = models.DateField(blank=False)
    sesh_type = models.CharField(max_length=1000)
    sesh_environ = models.CharField(max_length=1000)
    
    joining = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='joining')
    maybe = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='maybe')
    
    def __str__(self):
        return f"{self.user}_{self.date_posted}_{self.sesh_type}"
    
    
