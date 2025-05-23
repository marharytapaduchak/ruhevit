from django.http import JsonResponse
import json
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login
from .forms import RegisterForm
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.shortcuts import render


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        if form.is_valid():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Неправильне ім'я користувача або пароль")
        else:
            print(form.errors)
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


@csrf_exempt
def check_email(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email", "")
            exists = get_user_model().objects.filter(email=email).exists()
            return JsonResponse({"exists": exists})
        except Exception as e:
            return JsonResponse({"exists": False, "error": str(e)}, status=400)
    return JsonResponse({"detail": "Method not allowed"}, status=405)
