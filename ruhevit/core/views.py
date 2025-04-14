from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.shortcuts import render
from requests.models import Request
from django.contrib.auth.decorators import login_required


def home_redirect(request):
    if request.user.is_authenticated:
        user = request.user
        user_owner_requests = Request.objects.filter(owner=user).order_by('-created_at')
        user_exec_requests = Request.objects.filter(executor__isnull=False, executor=user).order_by('-created_at')
        help_offers = Request.objects.filter(status='pending').exclude(owner=user).order_by('-created_at')
        context = {
            'user_owner_requests': user_owner_requests,
            'user_exec_requests': user_exec_requests,
            'help_offers': help_offers,
        }
        return render(request, 'home/index.html', context)
    else:
        return render(request, 'landing/index.html')


def custom_404_view(request, exception):
    return render(request, 'errors/404.html', status=404)


def search_requests(request):
    query = request.GET.get('q', '')
    results = Request.objects.filter(name__icontains=query) if query else []
    return render(request, 'core/search_results.html', {'results': results, 'query': query})
