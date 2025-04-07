from django.contrib.auth import login
from .forms import RegisterForm
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.shortcuts import render


def auth(request):
    return render(request, 'accounts/auth.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # або на /dashboard/ чи інше
            else:
                form.add_error(None, 'Невірне ім’я користувача або пароль.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = form.cleaned_data['role']
            user.save()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})

def reset_pass(request):
    return render(request, 'accounts/password_reset.html')


def reset_pass_confirm(request):
    return render(request, 'accounts/new_password.html')
