from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def home(request):
    return render(request,'../templates/profile.html')

def user_login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the desired page after login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, '../templates/login2.html')

