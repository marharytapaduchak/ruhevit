from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.shortcuts import render
from requests.models import Request


def home_redirect(request):
    if request.user.is_authenticated:
        user = request.user
        user_requests = Request.objects.filter(
            owner=user).order_by('-created_at')
        help_offers = Request.objects.filter(status='pending').exclude(
            owner=user).order_by('-created_at')
        context = {
            'user_requests': user_requests,
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
