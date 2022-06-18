from logging.config import _LoggerConfiguration
from tkinter import CASCADE
from unicodedata import name
from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=30)
    posted = models.DateTimeField(auto_now_add=True)

class Neighborhood(models.Model):
    name = models.CharField(max_length=75)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
