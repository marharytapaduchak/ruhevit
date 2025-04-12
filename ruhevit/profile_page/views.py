from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from requests.models import Request, Review  # Припускаємо, що моделі розміщені у додатку requests

@login_required
def profile_page(request):
    user = request.user

    # Активні запити — наприклад, статуси pending, need_volunteer, in_progress
    active_statuses = ['pending', 'need_volunteer', 'in_progress']
    active_requests = Request.objects.filter(owner=user, status__in=active_statuses).order_by('-created_at')

    # help_offers = Request.objects.filter(status='need_volunteer').order_by('-created_at')

    # Історія запитів — виконані запити (status='done')
    history_requests = Request.objects.filter(owner=user, status='done').order_by('-created_at')

    # Відгуки щодо запитів, які створив користувач
    reviews = Review.objects.filter(request__owner=user)

    context = {
        'user': user,
        'active_requests': active_requests,
        'history_requests': history_requests,
        'reviews': reviews,
        # 'help_offers': help_offers,
    }
    return render(request, 'profile_page/index.html', context)
