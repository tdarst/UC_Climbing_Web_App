from django import forms
from .models import ClimbingSession
import datetime
from common import get_current_time

class ClimbingSessionForm(forms.ModelForm):
    date_going = forms.DateField(initial=datetime.date.today, required=True)
    time_going = forms.TimeField(initial=get_current_time, required=True)
    sesh_type = forms.CharField(max_length=1000, required=True)
    sesh_environ = forms.CharField(max_length=1000, required=True)
    location = forms.CharField(max_length=1000, required=True)
    
    class Meta:
        model = ClimbingSession
        fields = ['date_going', 'time_going', 'sesh_type', 'sesh_environ',  'location']
        
    def save(self, commit=True):
        sesh = super().save(commit=False)
        date_going = self.cleaned_data.get('date_going')
        time_going = self.cleaned_data.get('time_going')
        sesh_type = self.cleaned_data.get('sesh_type')
        sesh_environ = self.cleaned_data.get('sesh_environ')
        location = self.cleaned_data.get('location')
        
        if commit:
            sesh.save()
            
        return sesh