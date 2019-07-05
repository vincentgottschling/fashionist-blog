from django import forms
from .models import Post, About_Me, Events

class PostForm(forms.ModelForm):

    class Meta:
         model = Post
         fields = ('title', 'text', 'image', 'link')

class InfoForm(forms.ModelForm):

    class Meta:
         model = About_Me
         fields = ('name', 'age','hobbies','favourite_food','about_me')

class EventsForm(forms.ModelForm):

    class Meta:
        model = Events
        fields = ('title', 'text','event_date','event_time','image')
        labels = {
            "event_date": "Date of the Event ('DD.MM.YYYY')"
        }


         