from django import forms
from .models import Post, About_Me

class PostForm(forms.ModelForm):

    class Meta:
         model = Post
         fields = ('title', 'text','picture','link')

class InfoForm(forms.ModelForm):

    class Meta:
         model = About_Me
         fields = ('name', 'age','hobbies','favourite_food','about_me')