from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from requests.models import Request  # або як називається твоя модель

def index(request):
    all_requests = Request.objects.all()
    return render(request, 'home/index.html', {'all_requests': all_requests})
