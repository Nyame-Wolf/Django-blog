from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class CustomUser(AbstractUser):
    pass

class Post(models.Model):
     title = models.CharField(max_length=100)
     content = models.TextField()
     date_posted = models.DateTimeField(default=timezone.now)
     author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
     
     def __str__(self):
          return self.title