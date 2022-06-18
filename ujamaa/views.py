from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import RegisterForm,UpdateProfileForm,AddProjectForm,RatingForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
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
            return redirect('index.html')
    else:        
        form = RegisterForm()
    return render(request, 'register.html')    