from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """Register for a new user"""
    if request.method == 'POST':
        #Process complete form.
        form = UserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            # log in a new user and redirect to the index page.
            login(request, new_user)
            return redirect('to_do_list_app:index')
    else:
        #Display blank register
        form = UserCreationForm()
    
    #Display a blank or invalid form.
    context = {'form':form}
    return render(request, 'registration/register.html', context)