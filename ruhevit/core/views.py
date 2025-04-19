from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.shortcuts import render
from requests.models import Request
from django.contrib.auth.decorators import login_required


from requests.models import Request


def home_redirect(request):
    if request.user.is_authenticated:
        user = request.user
        user_owner_requests = Request.objects.filter(
            owner=user).order_by('-created_at')
        user_exec_requests = Request.objects.filter(
            executor__isnull=False, executor=user).order_by('-created_at')
        help_offers = Request.objects.filter(status='pending', executor__isnull=True).exclude(
            owner=user).order_by('-created_at')

        context = {
            'user_owner_requests': user_owner_requests,
            'user_exec_requests': user_exec_requests,
            'help_offers': help_offers,
        }
        return render(request, 'home/index.html', context)
    else:
        latest_requests = Request.objects.order_by('-created_at')[:3]
        volunteer_count = Request.objects.exclude(
            executor=None).values('executor').distinct().count()
        completed_count = Request.objects.filter(status='done').count()
        military_count = Request.objects.values('owner').distinct().count()

        return render(request, 'landing/index.html', {
            'latest_requests': latest_requests,
            'volunteer_count': volunteer_count,
            'completed_count': completed_count,
            'military_count': military_count
        })

def custom_404_view(request, exception):
    return render(request, 'errors/404.html', status=404)


def search_requests(request):
    query = request.GET.get('q', '')
    results = Request.objects.filter(name__icontains=query) if query else []
    return render(request, 'core/search_results.html', {'results': results, 'query': query})
