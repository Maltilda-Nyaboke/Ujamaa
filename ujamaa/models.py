from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django import forms


# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=30)
    posted = models.DateTimeField(auto_now_add=True)

class Neighborhood(models.Model):
    name = models.CharField(max_length=75)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo =models.ImageField(upload_to='images')
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE,null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
    joined=models.DateTimeField(auto_now=True)

class Business(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

class Post(models.Model):
    title = models.CharField(max_length=50)
    image =models.ImageField(upload_to='images')
    content = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, default=1)
    posted = models.DateTimeField(auto_now_add=True)    

