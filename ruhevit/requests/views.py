from django.shortcuts import get_object_or_404, redirect, render
from .forms import RequestHistoryForm
from django.shortcuts import render
from .models import Request


def main_page(request):
    requests = Request.objects.filter(
        status__in=['in_progress', 'need_volunteer']).order_by('-created_at')
    return render(request, 'requests/main_page.html', {'requests': requests})


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
