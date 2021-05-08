from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.views import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
import json
from .forms import profileForm
from .models import *

def index(request):
    print(matcher(6))
    return render(request,'index.html')


def createProfile(request):
    profileObj = Profile.objects.all()
    for p in profileObj:
            interestsList = p.interests.split()
            print(interestsList)
    if request.method == "POST":
        form = profileForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('createProfile')
        else:
            print('not valid')
    form = profileForm
    context = {'form':form}
    return render(request,'createProfile.html',context)


#the matcher method takes in a user and searches through all the other users
#to find the best matched user for the user in question. 
def matcher(userID):
    #geting the user
    user = Profile.objects.get(id = userID)
    userInterests = user.interests.split()
    allUsers = Profile.objects.exclude(id = userID)
    userList = []
    #searching through the whole list
    for profile in allUsers:
        interestWeight = 0
        for interest in userInterests:
            for other in profile.interests.split():
                if interest == other:
                    interestWeight = interestWeight + 1
        userList.append({"profile":profile,"weight":interestWeight})
    userList.sort(reverse=True,key=myFunc)
    return userList

def myFunc(e):
    return e["weight"]
                    
    

