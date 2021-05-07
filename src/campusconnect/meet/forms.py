from django import forms
from django.contrib.auth.forms import UserCreationForm
#from accounts.models import Account
from meet.models import Profile

#Tinashe Mukundi Chitamba
#This script deals with forms. It takes the data inputed in a form and populates
#a specific model of the database

#sellerform is used to register a new seller, after being registered as a user
class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profileImage','studentNumber','user','description','interests']
        #widgets = {'user': forms.HiddenInput()}
        