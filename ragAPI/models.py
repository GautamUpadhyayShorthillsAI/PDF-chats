from django.db import models

# Create your models here.
class User(models.Model):
    Fname = models.CharField(max_length=50)
    Lname = models.CharField(max_length=50)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=255)
    
class Chats(models.Model):
    userId = models.ForeignKey(User,on_delete=models.CASCADE)
    chat = models.CharField(max_length=500)
    response = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now=True)