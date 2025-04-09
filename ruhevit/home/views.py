from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from requests.models import Request  # Імпортуємо твою модель

@login_required
def index(request):
    user_requests = Request.objects.filter(owner=request.user)
    return render(request, 'home/index.html', {'user_requests': user_requests})
