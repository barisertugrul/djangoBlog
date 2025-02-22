from django.shortcuts import render, redirect
from .forms import RegisterForm

from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.

def loginUser(request):
    return render(request, 'login.html')

def register(request):
    """Register a new user."""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            newUser = User (
                username = username,
                email = email,
                first_name = first_name,
                last_name = last_name
            )
            newUser.set_password(password)
            newUser.save()

            login(request, newUser)

            return redirect('index')
        else:
            context = {
                'form': form
            }
            return render(request, 'register.html', context)

    else:
        form = RegisterForm()

        context = {
            'form': form
        }
        return render(request, 'register.html', context)

def logoutUser(request):
    pass
