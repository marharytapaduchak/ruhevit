from django.db.models import Q
from django.shortcuts import render
from requests.models import Request


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
            executor=user, status__in=['in_progress']).order_by('-created_at')

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
    context = {
        'error_code': 404,
        'error_message': 'Сторінку не знайдено'
    }
    return render(request, 'errors/404.html', context=context, status=404)


# Generic custom error view for other error codes (e.g., 403, 500)
def custom_error_view(request, error_code=500, error_message='Виникла помилка сервера'):
    context = {
        'error_code': error_code,
        'error_message': error_message
    }
    return render(request, 'errors/404.html', context=context, status=error_code)


def search_requests(request):
    query = request.GET.get('q', '').strip()
    results = []

    if query:
        results = Request.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(owner__username__icontains=query) |
            Q(owner__first_name__icontains=query) |
            Q(owner__last_name__icontains=query) |
            Q(executor__username__icontains=query) |
            Q(executor__first_name__icontains=query) |
            Q(executor__last_name__icontains=query)
        ).distinct()

    return render(request, 'core/search_results.html', {'results': results, 'query': query})
