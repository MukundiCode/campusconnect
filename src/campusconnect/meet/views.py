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


def createProfile(request):
    form = profileForm
    context = {'form':form}
    return render(request,'createProfile.html',context)
