from django.db import models
from django.db.models.base import Model
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    
    def __str__(self):
        return self.title

class Userdata(models.Model):
    name = models.CharField(max_length=200) 
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    day = models.PositiveIntegerField()
    gender = models.CharField(max_length=200) 
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.name



# Create your models here.
