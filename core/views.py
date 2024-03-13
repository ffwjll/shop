from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def signin(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'shop/signin.html', {
                'error': 'Error'
            })
        login(request, user)
        return redirect('profile')

    return render(request, 'shop/signin.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        password = request.POST['password']
        repeat_password = request.POST['repeat_password']
        if password != repeat_password:
            return render(request, 'shop/signup.html', {
                'error': 'Passwords did not match'
            })
        User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            password=password
        )
        return redirect('signin')
    return render(request, 'shop/signup.html')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    return render(request, 'shop/profile.html')


def signout(request):
    logout(request)
    return redirect('catalog')
