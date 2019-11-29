from django.shortcuts import render, redirect
from blog_app.forms import CustomUserCreationForm


def register(request):
    form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# Create your views here.
