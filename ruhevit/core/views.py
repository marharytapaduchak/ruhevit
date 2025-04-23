from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.shortcuts import render
from requests.models import Request
from django.contrib.auth.decorators import login_required


from requests.models import Request


def home_redirect(request):
    if request.user.is_authenticated:
        user = request.user
        from collections import Counter

        # Запити створені та прийняті користувачем
        user_created = Request.objects.filter(
            owner=user, status__in=['pending', 'active']).order_by('-created_at')

        user_accepted = Request.objects.filter(executor=user)

        # Об'єднані для аналізу
        user_related_requests = user_created | user_accepted

        # Витягуємо популярні типи, локації, пріоритети
        types = Counter(req.type for req in user_related_requests if req.type)
        locations = Counter(req.location for req in user_related_requests if req.location)
        priorities = Counter(req.priority for req in user_related_requests if req.priority)

        top_types = [item[0] for item in types.most_common(3)]
        top_locations = [item[0] for item in locations.most_common(3)]
        top_priorities = [item[0] for item in priorities.most_common(2)]

        user_owner_requests = Request.objects.filter(
            owner=user, status__in=['pending', 'in_progress']).order_by('-created_at')
        user_exec_requests = Request.objects.filter(
            executor__isnull=False, executor=user).order_by('-created_at')

        all_potential_requests = Request.objects.filter(
            status='pending',
            executor__isnull=True
        ).exclude(owner=user)

        from django.db.models import Case, When, IntegerField, Value
        personalized_requests = all_potential_requests.annotate(
            relevance_score=(
                Case(When(type__in=top_types, then=Value(1)), default=Value(0), output_field=IntegerField()) +
                Case(When(location__in=top_locations, then=Value(1)), default=Value(0), output_field=IntegerField()) +
                Case(When(priority__in=top_priorities, then=Value(1)), default=Value(0), output_field=IntegerField())
            )
        ).order_by('-relevance_score', '-created_at')

        help_offers = Request.objects.filter(status='pending', executor__isnull=True).exclude(
            owner=user).order_by('-created_at')

        context = {
            'user_owner_requests': user_owner_requests,
            'user_exec_requests': user_exec_requests,
            'help_offers': help_offers,
            'personalized_requests': personalized_requests,
            'top_types': top_types,
            'top_locations': top_locations,
            'top_priorities': top_priorities,
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
