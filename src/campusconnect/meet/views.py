from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.views import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
import json
from .forms import profileForm

def index(request):
    return render(request,'index.html')

def createEvent(request):
    return render(request,'createEvent.html')

def createProfile(request):
    if request.method == "POST":
        form = profileForm(request.POST)
        print(form)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('index')
        else:
            print('not valid')
    form = profileForm
    context = {'form':form}
    return render(request,'createProfile.html',context)
