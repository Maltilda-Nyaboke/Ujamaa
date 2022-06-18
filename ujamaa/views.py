from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import RegisterForm,UpdateProfileForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *

# Create your views here.

def home(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:        
        form = RegisterForm()
    return render(request, 'register.html',{'form':form}) 

def login_user(request):
    form = AuthenticationForm()
    context = {'form':form}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'registration/login.html',context)  
    else:
        return render(request, 'registration/login.html',context)  

def logout_user(request):
    logout(request)
    return redirect('login')                

def profile(request):
    user = request.user.pk
    profile = Profile.objects.all()
    profile = Profile.objects.filter(user=request.user.pk)
    context = {'profile': profile}
    return render(request, 'profile.html',context)  

def update_profile(request):
    form = UpdateProfileForm()
    user = request.user
    # profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile.profile_photo = form.cleaned_data.get('profile_photo')
            profile.bio = form.cleaned_data.get('bio')
            profile.save()
            return redirect('profile')
        else:
            form = UpdateProfileForm() 
    return render(request, 'update_profile.html',{'form':form})       