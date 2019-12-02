from django.shortcuts import render,redirect
from blog_app.forms import CustomUserCreationForm
from django.contrib import messages 
from django.contrib.auth.decorators  import login_required
from .forms import UserUpdateForm, ProfileUpdateFrom

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created. Enter your credentials to Log in')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateFrom(request.POST, request.FILES, instance=request.user.profile )
        if u_form.is_valid() & p_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request, f'Your Account has been updated!')
    else:
         u_form = UserUpdateForm(instance=request.user)
         p_form = ProfileUpdateFrom(instance=request.user.profile )
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html',context)