from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.utils.http import url_has_allowed_host_and_scheme

from .forms import RegisterForm, LoginForm

# Create your views here.

def loginUser(request):
    """Login a user."""
    form = LoginForm(request.POST or None)

    # Get the next URL
    next_url = request.GET.get('next') or request.POST.get('next')

    # Check if the next URL is safe
    if next_url and not url_has_allowed_host_and_scheme(
        url=next_url,
        allowed_hosts={request.get_host()},
        require_https=request.is_secure()
    ):
        next_url = None

    context = {
        'form': form,
        'next': next_url
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        authenticated_user = authenticate(username=username, password=password)

        if authenticated_user is not None:
            login(request, authenticated_user)
            messages.success(request, 'User logged in successfully.')

            if next_url:
                return redirect(next_url)
            return redirect('article:dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html', context)

def register(request):
    """Register a new user."""

    """Method 1"""
    """if request.method == 'POST':
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
        return render(request, 'register.html', context)"""

    """Method 2"""
    form = RegisterForm(request.POST or None)
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
        messages.success(request, 'User registered successfully.')

        return redirect('article:dashboard')

    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def logoutUser(request):
    """Logout a user."""
    logout(request)
    messages.success(request, 'User logged out successfully.')
    return redirect('index')
