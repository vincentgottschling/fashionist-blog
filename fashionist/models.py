from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    picture=models.CharField(max_length=500, blank=True)
    link=models.CharField(max_length=500, default='', blank=True)
    image = models.ImageField(upload_to='images/', default="C:/Users/vince/Desktop/fashionist/Bilder/Logo.png")
    CATEGORY_CHOICES=[
        ('HS','Hairstyle'),
        ('MU','Make-Up'),
        ('SH','Shoes'),
        ('AC','Accessoirs'),
        ('OD','Outfit of the Day'),
        ('EE','Everything Else')
    ]
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default='EE',
    )

    
    #Link zu Kleidungsstücken, z.B. Amazon
    #Likes
    #pictures

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class About_Me(models.Model):
    name=models.CharField(max_length=200, default='')
    age=models.CharField(max_length=200, default='')
    hobbies=models.CharField(max_length=200, default='')
    favourite_food=models.CharField(max_length=200, default='')
    about_me=models.TextField(default='')

class Events(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    event_date=models.DateField()
    event_time=models.TimeField()
    location=models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
