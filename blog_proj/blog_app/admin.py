from django.contrib import admin
from django.contrib.auth import get_user_model # gets the custom user model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Post

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = get_user_model()
    list_display = ['email', 'username']

admin.site.register(get_user_model(), CustomUserAdmin) #to see the custom user on django admin page.
admin.site.register(Post) #to see the Post model on django admin page.

