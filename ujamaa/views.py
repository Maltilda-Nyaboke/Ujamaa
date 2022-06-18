from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import RegisterForm
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