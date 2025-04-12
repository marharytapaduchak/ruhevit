from django.shortcuts import render

def profile_page(request):
    return render(request, 'profile_page/index.html')
