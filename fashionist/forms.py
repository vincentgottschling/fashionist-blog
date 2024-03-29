from django import forms
from .models import Post, About_Me, Events

class PostForm(forms.ModelForm):

    class Meta:
        model = Post 
        fields = ('title', 'text','category', 'image', 'link')

class InfoForm(forms.ModelForm):

    class Meta:
        model = About_Me
        fields = ('image','about_me')

class EventsForm(forms.ModelForm):

    class Meta:
        model = Events
        fields = ('title', 'text','event_date','event_time', 'location' ,'image')
        labels = {
            "event_date": "Date of the Event (dd.mm.yyyy)",
            "event_time": "Time of the Event (hh:mm)"
        }


         