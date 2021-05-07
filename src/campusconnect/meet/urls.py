from meet import views
from django.urls import path

#this file contains the url patterns for the web application

urlpatterns = [
    path('createProfile', views.createProfile,name='createProfile'),
]