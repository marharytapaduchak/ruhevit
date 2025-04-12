from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from requests.models import Request, Review

@login_required
def profile_page(request):
    user = request.user

    # Активні запити — беремо ті, що не виконані (наприклад, стан pending, need_volunteer або in_progress)
    active_statuses = ['pending', 'need_volunteer', 'in_progress']
    active_requests = Request.objects.filter(owner=user, status__in=active_statuses).order_by('-created_at')

    # Історія запитів — виконані запити (status='done')
    history_requests = Request.objects.filter(owner=user, status='done').order_by('-created_at')

    # Відгуки, що стосуються запитів користувача
    reviews = Review.objects.filter(request__owner=user).order_by('-date')

    context = {
        'user': user,
        'active_requests': active_requests,
        'history_requests': history_requests,
        'reviews': reviews,
    }
    return render(request, 'profile_page/index.html', context)
