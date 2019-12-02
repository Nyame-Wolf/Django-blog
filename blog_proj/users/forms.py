from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']

class ProfileUpdateFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']