from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=8)  
    email = models.EmailField(unique=True)



class ChatResponse(models.Model):
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, related_name='chats')
    chat = models.TextField()
    response = models.TextField()
    time = models.DateTimeField(default=timezone.now)
