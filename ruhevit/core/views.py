from django.shortcuts import render

def home_redirect(request):
    if request.user.is_authenticated:
        return render(request, 'profile_page/index.html')
    else:
        return render(request, 'landing/index.html')
