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

#def matcher(user):

