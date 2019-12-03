#we register the signals in apps.py file
#automatically add a profile to a user on registration

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile

#creates the signal
@receiver(post_save, sender=get_user_model())
def create_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#save the signal
@receiver(post_save, sender=get_user_model())
def save_profile(sender,instance, **kwargs):
    instance.profile.save()
