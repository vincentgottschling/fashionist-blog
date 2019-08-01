from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),                            #Startseite
    path('news/<int:pk>/', views.news_detail, name='news_detail'),          #Detailansicht
    path('post/news/', views.new_news, name='new_news'),                    #Beitrag erstellen
    path('post/<int:pk>/edit/', views.news_edit, name='news_edit'),         #Beitrag bearbeiten
    path('about_me/',views.about_me,name='about_me'),                       #About Me
    path('about_me/edit/',views.edit_info,name='edit_info'),                #About Me bearbeiten
    path('events/',views.events,name='events'),                             #Events
    path('events/add/', views.new_events, name='new_events'),               #Event erstellen 
    path('events/<int:pk>/edit/', views.events_edit, name='events_edit'),   #Events bearbeiten
]