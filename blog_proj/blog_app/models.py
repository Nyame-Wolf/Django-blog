from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.urls import reverse

# create a custom user as recommended by django doc 
class CustomUser(AbstractUser):
    pass

class Post(models.Model):
     title = models.CharField(max_length=100)
     content = models.TextField()
     date_posted = models.DateTimeField(default=timezone.now)
     author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
     
     # make the post object more descriptive
     def __str__(self):
          return self.title
    
    #let django know how to find location of a specific post which allows the post creation cbv to redirect us to the new post's detail page  
     def get_absolute_url(self):
         return reverse('post-detail', kwargs={'pk':self.pk})