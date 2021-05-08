from django.db import models
from django.conf import settings
from PIL import Image


class Profile(models.Model):
    #sellerID automatically inserted by Django
    user = models.OneToOneField(settings.AUTH_USER_MODEL,null=True, on_delete=models.CASCADE)
    profileImage = models.ImageField(null = True, blank = True,help_text='Add an picture for your profile',)
    studentNumber = models.CharField(max_length=9, default= 0)
    values = models.CharField(null=True,max_length=250,help_text="Write at least three of the vaues you hold dearly, eg, liberal,Christian. Write in the form value1 value2 value3...")
    interests = models.CharField(null=True,max_length=800,help_text="Write your interest here in this format: interest1 interest2 interest3... You can put as many as you want to.") # JSON-serialized (text) version of your list
    description = models.TextField(null=True,max_length=200,help_text='Take this opportunity to describe yourself! Feel free to say anything or everything about what defines you as a person.',)
    yearOfStudy = models.IntegerField(null=True, help_text="What is your current year of study? This helps us match you with people within your age bracket.")

    def __str__(self):
        return self.user.username

class MeetUp(models.Model):
    title = models.CharField(null=True,max_length=100,help_text="Give your meetup request a title, eg , 'Looking for a group of friends to go hiking with'.Try to keep it short.")
    location = models.CharField(null=True, max_length=100,help_text="Where would you want to meet ?If anywhere on campus, just say On Campus.")
    time = models.CharField(null=True,max_length=10,help_text="At around what time of the day would you want to meet?")
    description = models.TextField(null= True,help_text="Give a description about the type of meetup this would be. Is it an activity (hiking, skiing etc), or just chilling at a public place on campus.")
    numberOfPeople = models.IntegerField(null=True,default=1,help_text="How many people would you like us to notify? Due to covid protocols, we can only allow a maximum of 3 people.")

class Meet_User(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,null = True,on_delete = models.CASCADE)
    meetup = models.ForeignKey(MeetUp,null = True,on_delete = models.CASCADE)

class Event(models.Model):
    title = models.CharField(null=True,max_length=30,help_text="What is the name of your event")
    date = models.CharField(null = True,max_length=12,help_text="When is your event?")
    poster = models.ImageField(null = True, blank = True,help_text='Add a poster for this evet',)
    limit = models.IntegerField(null=True,help_text="How many people should be at this event")
    
class Requests(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,null = True,on_delete = models.CASCADE,related_name="user")
    meetup = models.ForeignKey(MeetUp,null = True,on_delete = models.CASCADE)
    requestee = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.CASCADE,related_name="requestee")