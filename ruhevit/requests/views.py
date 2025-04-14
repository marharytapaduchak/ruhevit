from django.shortcuts import get_object_or_404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Request, RequestHistory, RequestPhoto


@login_required
def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.status = 'pending'
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


@login_required
def report_confirm(request):
    return render(request, 'report_confirm/index.html')


def request_view(request, request_id):
    return request_detail(request, request_id)


@login_required
def report_submit(request, request_id):
    req_obj = get_object_or_404(Request, id=request_id)

    if request.method == 'POST':
        form = RequestHistoryForm(request.POST, request.FILES)
        if form.is_valid():
            history = form.save(commit=False)
            history.request = req_obj
            history.status = 'in_progress'
            history.save()

            req_obj.status = 'done'
            req_obj.save()

            uploaded_photos = request.FILES.getlist('photos[]')
            for photo in uploaded_photos:
                RequestPhoto.objects.create(history=history, image=photo)

            return redirect('request_detail', request_id=req_obj.id)
    else:
        form = RequestHistoryForm()

    return render(request, 'report_submit/index.html', {
        'form': form,
        'request_obj': req_obj,
    })

@login_required
def request_detail(request, request_id):
    request_obj = get_object_or_404(Request, pk=request_id)
    history = request_obj.history.select_related('request').prefetch_related('photos').order_by('-date')
    return render(request, 'request_view/index.html', {
        'request_obj': request_obj,
        'history': history
    })

@login_required
def confirm_request(request, request_id):
    print("⚙️ Працює confirm_request")
    req_obj = get_object_or_404(Request, id=request_id)

    print("Поточний виконавець:", req_obj.executor)
    print("Поточний ініціатор:", req_obj.owner)

    if not req_obj.executor:
        req_obj.executor = request.user
        req_obj.status = 'in_progress'
        req_obj.save()

        history_entry = RequestHistory.objects.create(
            request=req_obj,
            status='in_progress',
            comment=f"{request.user.get_username()} підтвердив запит"
        )

        print(f"✅ Призначено виконавця: {req_obj.executor.username}")
    else:
        print("❌ Виконавець вже був призначений:", req_obj.executor)

    return redirect('request_detail', request_id=req_obj.id)
