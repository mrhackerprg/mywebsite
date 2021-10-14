from django.db import models
from django.db.models.base import Model

# Create your models here.

class Info(models.Model):
    title = models.CharField(max_length = 100 , blank = True)
    artist = models.CharField(max_length = 100 , blank = True)
    aboutme = models.CharField(max_length = 225 , blank = True)
    aboutmetwo = models.CharField(max_length = 225 , blank = True)
    phonenumber = models.CharField(max_length = 15 , blank = True)
    email = models.EmailField(blank = True)
    twitter = models.CharField(max_length = 255 , blank = True)
    facebookchat = models.CharField(max_length = 20 , blank = True)

class Musics(models.Model):
    music1 = models.CharField(max_length = 25 , blank = True)
    music2 = models.CharField(max_length = 25 , blank = True)
    music3 = models.CharField(max_length = 25 , blank = True)
    music4 = models.CharField(max_length = 25 , blank = True)
    aboutmusics = models.CharField(max_length = 225 , blank = True)

class MusicsInfo(models.Model):
    music1about = models.CharField(max_length = 25 , blank = False)
    music2about = models.CharField(max_length = 25 , blank = False)
    music3about = models.CharField(max_length = 25 , blank = False)
    music3about = models.CharField(max_length = 25 , blank = False)

class SendMessage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 25 , blank = False)
    email = models.EmailField()
    subject = models.CharField(max_length = 50 , blank = False)
    message = models.CharField(max_length = 225 , blank = False)