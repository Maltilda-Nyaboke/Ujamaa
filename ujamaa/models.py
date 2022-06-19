from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django import forms


# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=30)
    posted = models.DateTimeField(auto_now_add=True)

    def save_location(self):
        self.save()

    def __str__(self):
        return self.name


class Neighborhood(models.Model):
    name = models.CharField(max_length=75)
    image =models.ImageField(upload_to='images')
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    occupants_count = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def create_neigborhood(self):
        self.save()

    def delete_neigborhood(self):
        self.delete() 

    def update_neigborhood(self):
        self.update()        


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo =models.ImageField(upload_to='images')
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE,null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
    joined=models.DateTimeField(auto_now=True)

    def save_profile(self):
        self.save()

class Business(models.Model):
    name = models.CharField(max_length=50)
    image =models.ImageField(upload_to='images')
    email = models.EmailField(max_length=50)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self):
        self.update()   

    def __str__(self):
        return self.name     

class Post(models.Model):
    title = models.CharField(max_length=50)
    image =models.ImageField(upload_to='images')
    content = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, default=1)
    posted = models.DateTimeField(auto_now_add=True)    

