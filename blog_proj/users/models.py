from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')#automatically creates a profile_pics dir. we however change settings setting MEDIA_URL and MEDIA_ROOT so as not to clutter primary dir


    def __str__(self):
        return f'{self.user.username} Profile'
    
    #override save method so as to automatically resize photos to maximise performance. Other methods are available.
    def save(self, *args, **kwargs):
       super().save(*args, **kwargs) # Call the real save() method

       img = Image.open(self.image.path)

       if img.height > 300 or img.width > 300:
           output_size = (300,300)
           img.thumbnail(output_size)
           img.save(self.image.path)

