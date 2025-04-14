from django.shortcuts import render

def changing_info(request):
    return render(request, 'changing_info/index.html')
