"""Views for authentication app"""
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from .forms import CreateUserForm


def home_page(request:HttpRequest)->HttpResponse:
    """
    Home page endpoint

    Args:
        request (HttpRequest): request from frontend

    Returns:
        HttpResponse: renderized response of home.html
    """
    return render(request, 'home.html')

def register_page(request:HttpRequest)->HttpResponse:
    """
    Registe page endpoint

    Args:
        request (HttpRequest): request from frontend

    Returns:
        HttpResponse: renderized response of home.html
    """
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            messages.success(request,'Account Created Successfully for' +user)
            return redirect('authentication:login')

    return render(request, 'registerPage.html', {'form':form})

def login_page(request:HttpRequest)->HttpResponse:
    """
    Login page endpoint

    Args:
        request (HttpRequest): request from frontend

    Returns:
        HttpResponse: renderized response of home.html
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('')

        messages.info(request,'Username or Password is incorrect')
        return redirect('authentication:login')


    return render(request, 'loginpage.html')

@login_required(login_url='authentication:login')
def logout_page(request:HttpRequest)->HttpResponse:
    """
    Logout page endpoint

    Args:
        request (HttpRequest): request from frontend

    Returns:
        HttpResponse: renderized response of home.html
    """
    logout(request)
    return redirect('home')
