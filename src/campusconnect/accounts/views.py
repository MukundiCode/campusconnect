from django.shortcuts import render

from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as django_login, logout as django_logout

def register(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print('The form is valid')
            user = form.save()
            print(form)
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            #user = authenticate(email=email,password = password)
            django_login(request, user)
            return redirect('index')
        else:
            print(form.errors)
            form_error = True
            context = {'form':form,'form_error':form_error}
            return render(request,'registration/register.html',context)
    else:
        form = RegistrationForm()
        #context['registration_form'] = form
        context = {'form':form}
    #return render(request,'registration/register.html', context )
    return render(request,'registration/register.html')

def login(request):
    context = {}
    #request.META['HTTP_REFERER'] MIGHT NEED THIS LATER TO REDRECT TO LAST PAGE UPON LOGIN
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        print(request.POST.get('Email'))
        user = authenticate(request,email=email,password = password)
        if user != None:
            django_login(request, user)
            return redirect('index')
        else:
            error_message = "Email or Password incorrect, please try again"
            context = {'error':error_message}
            return render(request,'registration/login.html',context)
    return render(request,'registration/login.html',context)

def logoutUser(request):
    #auth.logout(request)
    django_logout(request)
    return redirect('index')
