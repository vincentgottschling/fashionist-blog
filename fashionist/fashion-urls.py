from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('trends/', views.trends, name='trends'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('post/news/', views.new_news, name='new_news'),
    path('post/<int:pk>/edit/', views.news_edit, name='news_edit'),
    path('about_me/',views.about_me,name='about_me'),
    path('about_me/edit/',views.edit_info,name='edit_info'),
    path('events/',views.events,name='events'),
    path('events/add/', views.new_events, name='new_events'),
    path('events/<int:pk>/edit/', views.events_edit, name='events_edit'),
]