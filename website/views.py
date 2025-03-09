from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record

def home(request):

    records = Record.objects.all()

    # Is the user logging in?
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        # Authenticate our user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in.")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in.")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "You've been logged out.")
    return redirect('home')



    
