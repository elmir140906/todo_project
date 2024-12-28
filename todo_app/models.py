from django.db import models
from  django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date = models.DateField(default=datetime.now)
   
class Task(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    description = models.CharField(max_length=255) 
    is_done = models.BooleanField(default=False)