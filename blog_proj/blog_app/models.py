from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.urls import reverse

class CustomUser(AbstractUser):
    pass

class Post(models.Model):
     title = models.CharField(max_length=100)
     content = models.TextField()
     date_posted = models.DateTimeField(default=timezone.now)
     author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
     
     def __str__(self):
          return self.title

     def get_absolute_url(self):
         return reverse('post-detail', kwargs={'pk':self.pk})