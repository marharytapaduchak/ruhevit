from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import *
from django.shortcuts import render
from .models import Request


@login_required
def main_page(request):
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return redirect('create_request')
    else:
        form = RequestForm()

    requests = Request.objects.all()

    return render(request, 'requests/main_page.html', {
        'form': form,
        'requests': requests
    })


def submit_report(request, request_id):
    req = get_object_or_404(Request, id=request_id)

    if request.method == 'POST':
        form = RequestHistoryForm(request.POST, request.FILES)
        if form.is_valid():
            history = form.save(commit=False)
            history.request = req
            history.save()
            # або куди тобі треба
            return redirect('request_detail', request_id=req.id)
    else:
        form = RequestHistoryForm()

    return render(request, 'requests/submit_report.html', {'form': form, 'request_obj': req})
