from meet import views
from django.urls import path

#this file contains the url patterns for the web application

urlpatterns = [
    path('createProfile', views.createProfile,name='createProfile'),
    path('createEvent', views.createEvent,name='createEvent'),
    path('profile', views.profile,name='profile'),
    path('createRequest', views.createRequest,name='createRequest'),
    path('viewRequest/<requestID>',views.viewRequest,name='viewRequest'),
    path('acceptRequest/<requestID>',views.acceptRequest,name='acceptRequest'),
]
