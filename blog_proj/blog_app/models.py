from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager


# create a custom user as recommended by django doc
class CustomUser(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    tags = TaggableManager()

    class Meta:
        ordering = [
            "-date_posted"
        ]  # to order posts. since we want newest first we use -ve

    # make the post object more descriptive
    def __str__(self):
        return self.title

    # let django know how to find location of a specific post which allows the post creation cbv to redirect us to the new post's detail page
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return f"Comment by {self.name} on {self.post} "

