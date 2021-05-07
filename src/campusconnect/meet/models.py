from django.db import models
from django.conf import settings
from PIL import Image


class Profile(models.Model):
    #sellerID automatically inserted by Django
    user = models.OneToOneField(settings.AUTH_USER_MODEL,null=True, on_delete=models.CASCADE)
    profileImage = models.ImageField(null = True, blank = True,help_text='Add an picture for your profile',)
    studentNumber = models.IntegerField(max_length=10, default= 0)
    description = models.CharField(max_length=200,help_text='Add a brief description about yourself',)
    interests = models.TextField(null=True) # JSON-serialized (text) version of your list

