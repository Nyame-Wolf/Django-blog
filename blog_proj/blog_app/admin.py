from django.contrib import admin
from django.contrib.auth import get_user_model # gets the custom user model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Post,Comment

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = get_user_model()
    list_display = ['email', 'username']

admin.site.register(get_user_model(), CustomUserAdmin) #to see the custom user on django admin page.
admin.site.register(Post) #to see the Post model on django admin page.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
    actions = ['disable_comments','approve_comments']

    def disable_comments(self, request, queryset):
        queryset.update(active=False)

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


