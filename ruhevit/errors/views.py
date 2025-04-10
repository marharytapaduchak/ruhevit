from django.shortcuts import render

def errors(request):
    return render(request, 'errors/404.html')
