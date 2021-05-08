from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.views import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
import json
from .forms import profileForm, eventForm, meetupForm
from .models import *
from django.core.mail import send_mail

def index(request):
    return render(request,'index.html')

def createEvent(request):
    if request.method == "POST":
        form = eventForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('index')
        else:
            print('not valid')
    return render(request,'createEvent.html')

def profile(request):
    return render(request,'profile.html')

def createProfile(request):
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

def createRequest(request):
    #this user
    if request.METHOD == "POST":
        form = meetupForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('index')
        else:
            print('not valid')

        thisUserID = request.user
        user = Profile.objects.get(user = thisUserID)
        weightList = matcher(user.id)
        #sending emails
        for i in range(3):
            #creating the request for each user 
            request_obj = Requests(user=weightList[i]["profile"].user, meetup=form)
            request_obj.save()
            email_from = "tmchitamba@gmail.com"
            email_to = weightList[i]["profile"].user.email
            message = "Hey, someone wants to meet you"
            if message != '':
                send_mail(
                'Meeting request '+ email_from +' via campusConnect',
                message,
                email_from,
                [email_to],
                    )
                message = "Your email has been sent, and the seller will respond to you."
                print("message")
            else:
                message = "Can not send an empty email."

    form = profileForm
    context = {'form':form}
    return render(request,'createEvent.html',context)



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
