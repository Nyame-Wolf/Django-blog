from django.shortcuts import render,redirect
from blog_app.forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usename')
            return redirect('blog-home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

