from django.db import models
from django.conf import settings
from PIL import Image


class Profile(models.Model):
    #sellerID automatically inserted by Django
    user = models.OneToOneField(settings.AUTH_USER_MODEL,null=True, on_delete=models.CASCADE)
    profileImage = models.ImageField(null = True, blank = True,help_text='Add an picture for your profile',)
    studentNumber = models.CharField(max_length=9, default= 0)
    description = models.CharField(max_length=200,help_text='Add a brief description about yourself',)
    interests = models.TextField(null=True) # JSON-serialized (text) version of your list
    values = models.TextField(null=True)
    yearOfStudy = models.IntegerField(null=True)

class MeetUp(models.Model):
    location = models.CharField(null=True, max_length=100)
    time = models.CharField(null=True,max_length=10)
    description = models.TextField(null= True)

class Meet_User(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,null = True,on_delete = models.CASCADE)
    meetup = models.ForeignKey(MeetUp,null = True,on_delete = models.CASCADE)

class Event(models.Model):
    date = models.DateTimeField(null = True)
    poster = models.ImageField(null = True, blank = True,help_text='Add a poster for this evet',)
    limit = models.IntegerField(null=True)
    
class Requests(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,null = True,on_delete = models.CASCADE)
    meetup = models.ForeignKey(MeetUp,null = True,on_delete = models.CASCADE)
    #requester = models.OneToOneField(settings.AUTH_USER_MODEL,null=True, on_delete=models.CASCADE)