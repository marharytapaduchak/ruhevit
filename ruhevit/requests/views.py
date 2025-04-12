from django.shortcuts import render, get_object_or_404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Request


@login_required
def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.status = 'need_volunteer'
            instance.save()
            return redirect('requests:create_request')
    else:
        form = RequestForm()

    requests = Request.objects.all()

    return render(request, 'requests/main_page.html', {
        'form': form,
        'requests': requests
    })


@login_required
def submit_report(request, request_id):
    req = get_object_or_404(Request, id=request_id)

    if request.method == 'POST':
        form = RequestHistoryForm(request.POST, request.FILES)
        if form.is_valid():
            history = form.save(commit=False)
            history.request = req
            history.save()

            return redirect('request_detail', request_id=req.id)
    else:
        form = RequestHistoryForm()

    return render(request, 'requests/submit_report.html', {'form': form, 'request_obj': req})


def report_confirm(request):
    return render(request, 'report_confirm/index.html')


def request_view(request):
    return render(request, 'request_view/index.html')


def report_submit(request):
    return render(request, 'report_submit/index.html')


@login_required
def request_detail(request, request_id):
    request_obj = get_object_or_404(Request, pk=request_id)
    return render(request, 'request_view/index.html', {
        'request_obj': request_obj
    })
