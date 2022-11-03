from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    username = models.CharField(max_length=264)
    password = models.CharField(max_length=264)
    phoneno = models.CharField(max_length=264)
    gmailid = models.CharField(max_length=264)
    dob = models.CharField(max_length=264)
    # profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.username

class adhardocument(models.Model):
    phoneno=models.CharField(max_length=264,unique=True)
    adhaarno=models.CharField(max_length=264,unique=True)
    adhaar=models.ImageField(upload_to='images')

class passportdocument(models.Model):
    phoneno=models.CharField(max_length=264,unique=True)
    passportno=models.CharField(max_length=264,unique=True)
    passport=models.ImageField(upload_to='images')

class dldocument(models.Model):
    phoneno=models.CharField(max_length=264,unique=True)
    dlno=models.CharField(max_length=264,unique=True)
    dl=models.ImageField(upload_to='images')

class pancarddocument(models.Model):
    phoneno=models.CharField(max_length=264,unique=True)
    pancardno=models.CharField(max_length=264,unique=True)
    pancard=models.ImageField(upload_to='images')

class voteriddocument(models.Model):
    phoneno=models.CharField(max_length=264,unique=True)
    voteridno=models.CharField(max_length=264,unique=True)
    voterid=models.ImageField(upload_to='images')

class rationcarddocument(models.Model):
    phoneno=models.CharField(max_length=264,unique=True)
    rationcardno=models.CharField(max_length=264,unique=True)
    rationcard=models.ImageField(upload_to='images')

class buspassdocument(models.Model):
    phoneno=models.CharField(max_length=264,unique=True)
    buspassno=models.CharField(max_length=264,unique=True)
    buspass=models.ImageField(upload_to='images')

class Docstatus(models.Model):
    vstat=models.CharField(max_length=264)
    phoneno=models.CharField(max_length=264)
    addharstatus=models.CharField(max_length=264)
    passportstatus=models.CharField(max_length=264)
    dlstatus=models.CharField(max_length=264)
    pancardstatus=models.CharField(max_length=264)
    voteridstatus=models.CharField(max_length=264)
    rationcardstatus=models.CharField(max_length=264)
    buspassstatus=models.CharField(max_length=264)
