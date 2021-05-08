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
    #out index page will display requests if the user is aunthenticated
    if request.user.is_authenticated:
        requests = Requests.objects.filter(user = request.user)
        print(requests)
        context = {'requests':requests}
        return render(request,'index.html',context)
    return render(request,'index.html')

@login_required(login_url='login')
def createEvent(request):
    if request.method == "POST":
        form = eventForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('index')
        else:
            print('not valid')
    form = eventForm
    context = {'form':form}
    return render(request,'createEvent.html', context)

@login_required(login_url='login')
def createProfile(request):
    if request.method == "POST":
        form = profileForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('profile')
        else:
            print('not valid')
    form = profileForm
    context = {'form':form}
    return render(request,'createProfile.html',context)

@login_required(login_url='login')
def profile(request):
    user = Profile.objects.get(user = request.user)
    context = {'profile':user}
    return render(request,'profile.html',context)

@login_required(login_url='login')
def createRequest(request):
    #this user
    if request.method == "POST":
        form = meetupForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
        else:
            print('not valid')
            context = {'form':form}
            return render(request,'createRequest.html',context)

        thisUserID = request.user
        user = Profile.objects.get(user = thisUserID)
        weightList = matcher(user.id)
        print("Weight List", weightList)
        meetup = MeetUp.objects.latest('id')
        #sending emails
        for i in range(meetup.numberOfPeople):
            #creating the request for each user 
            request_obj = Requests(user=weightList[i]["profile"].user, meetup=meetup,requestee=request.user)
            request_obj.save()
            email_from = "tmchitamba@gmail.com"
            email_to = weightList[i]["profile"].user.email
            message = "Hey, "+ weightList[i]["profile"].user.username +", we have matched you up with "+user.user.username +" , who is having a meetup at "+meetup.location +". Log on to CampusConnect to accept of deny this request."
            if message != '':
                send_mail(
                'Meetup request '+ weightList[i]["profile"].user.username +' via campusConnect',
                message,
                email_from,
                [email_to],
                    )
                message = "Your email has been sent, and the seller will respond to you."
                print("message")
            else:
                message = "Can not send an empty email."
        msg = "Your meetup request has been sent. We will match you up with students with similar interests as you and notify you once they accept the invitation. "
        return redirect('message',msg)

    form = meetupForm
    context = {'form':form}
    return render(request,'createRequest.html',context)

def message(request,msg):
    if request.method == "POST":
        return redirect('index')
    context = {'message':msg}
    return render(request,"message.html",context)

@login_required(login_url='login')
def viewRequest(request,requestID):
    requests = Requests.objects.filter(user = request.user)
    req = Requests.objects.get(id = requestID)
    context = {'req':req,'requests':requests}
    return render(request,"viewRequest.html",context)

def acceptRequest(request,requestID):
    req = Requests.objects.get(id = requestID)
    meet_user_obj = Meet_User(user=request.user,meetup=req.meetup)
    meet_user_obj.save()
    #emailing the owner of the listing
    email_from = "tmchitamba@gmail.com"
    email_to = request.user.email
    message = "Hey, "+ req.requestee +",  "+request.user.username +" , has accepted your request to meetup. You can contact them on this email:"+request.user.email +". Remember to adhere to covid protocols in your interactions."
    if message != '':
        send_mail(
        'Meetup accepted via campusConnect',
        message,
        email_from,
        [email_to],
            )
        message = "Your email has been sent, and the seller will respond to you."
        print("Email sent")
    else:
        message = "Can not send an empty email."
    msg = "You've accepted the meetup request. We will notify "+req.requestee.user.username +". The will contact you via email. Remeber to observe covid protocols in your interactions. Happy mingling!"
    return redirect('message',msg)

def denyRequest(request,requestID):
    req = Requests.objects.get(id = requestID)
    req.delete()
    msg = "Request cancelled"
    return redirect('message',msg)

    

#the matcher method takes in a user and searches through all the other users
#to find the best matched user for the user in question. 
def matcher(userID):
    #geting the user
    user = Profile.objects.get(id = userID)
    userInterests = user.interests.split()
    userValues = user.values.split()
    allUsers = Profile.objects.exclude(id = userID)
    userList = []
    #searching through the whole list
    for profile in allUsers:
        interestWeight = 0
        for interest in userInterests:
            for other in profile.interests.split():
                if interest == other:
                    interestWeight = interestWeight + 1
        for values in userValues:
            for other in profile.values.split():
                if values == other:
                    interestWeight = interestWeight + 3
        userList.append({"profile":profile,"weight":interestWeight})
    userList.sort(reverse=True,key=myFunc)
    print(userList)
    return userList

def myFunc(e):
    return e["weight"]
                    
    

