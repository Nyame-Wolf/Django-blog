from django.shortcuts import render,redirect
from blog_app.forms import CustomUserCreationForm
from django.contrib import messages 


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('blog-home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

