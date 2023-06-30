from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from . import models


class LoginForm(AuthenticationForm) :
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control w-full py-3 px-6 rounded-xl','placeholder':'Username'}))
    password= forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control w-full py-3 px-6 rounded-xl','placeholder':'Password'}))
    
class SignupForm(UserCreationForm) :
    class Meta :
        model=User
        fields =( 'username','email','password1','password2')
        
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'class':'form-control w-full py-3 px-6 rounded-xl','placeholder':'Username'}))
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control w-full py-3 px-6 rounded-xl','placeholder':'Email'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control w-full py-3 px-6 rounded-xl','placeholder':'Password'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control w-full py-3 px-6 rounded-xl','placeholder':'Confirm Password'}))
    
class NewTourn(forms.ModelForm) :
    name=forms.CharField(label='Tournament Name',widget=forms.TextInput(attrs={'class':'form-control w-full py-3 px-6 rounded-xl','placeholder':'Tournament Name'}))
    no_of_teams=forms.IntegerField(label='Number of Teams',widget=forms.Select(choices=[("{}".format(i),"{}".format(i)) for i in range(2,27,2)],attrs={'class':'form-control w-full py-3 px-6 rounded-xl','placeholder':'Number of Teams'}))
    
    class Meta : 
        model = models.Tournament
        fields=('name','no_of_teams')