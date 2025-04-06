from django.shortcuts import render
from .models import Request


def main_page(request):
    requests = Request.objects.filter(
        status__in=['in_progress', 'need_volunteer']).order_by('-created_at')
    return render(request, 'requests/main_page.html', {'requests': requests})
