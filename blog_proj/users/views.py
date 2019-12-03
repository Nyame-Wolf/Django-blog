from django.shortcuts import render,redirect
from blog_app.forms import CustomUserCreationForm
from django.contrib import messages 
from django.contrib.auth.decorators  import login_required # the decorator ensures a user is logged in and redirects user to login if they try to access profile page and they are logged out
from .forms import UserUpdateForm, ProfileUpdateFrom

def register(request):
    if request.method == 'POST': 
        form = CustomUserCreationForm(request.POST) # request.POST adds data from our forms 
        if form.is_valid(): # Validates to see if the data given is valid
            form.save() #saves a new user to database
            username = form.cleaned_data.get('username') # Retrieves the saved user's username form the .cleanded_data dictionary
            messages.success(request, f'Your Account has been created. Enter your credentials to Log in') # returns a flash message to inform us a user has been added
            return redirect('login') # Redirects new user to login page
    else:
        form = CustomUserCreationForm() # renders an empty form
    return render(request, 'users/register.html', {'form': form})

# We have to set this in settings.py so that a user is redirected to login pageLOGIN_URL = 'login'
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user) # returns form populated with current user details.
        p_form = ProfileUpdateFrom(request.POST, request.FILES, instance=request.user.profile ) # returns form populated with current profile and current profile image.
        if u_form.is_valid() & p_form.is_valid(): # vaidates that both forms are valid
            p_form.save()
            u_form.save()
            messages.success(request, f'Your Account has been updated!')
            return redirect('profile')
    else:
         u_form = UserUpdateForm(instance=request.user)
         p_form = ProfileUpdateFrom(instance=request.user.profile )
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html',context)