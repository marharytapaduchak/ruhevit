from django.shortcuts import render


def auth(request):
    return render(request, 'accounts/auth.html')


def login(request):
    return render(request, 'accounts/login.html')


def signup(request):
    return render(request, 'accounts/signup.html')


def reset_pass(request):
    return render(request, 'accounts/password_reset.html')


def reset_pass_confirm(request):
    return render(request, 'accounts/new_password.html')
