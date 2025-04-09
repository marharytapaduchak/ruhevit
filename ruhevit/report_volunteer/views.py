from django.shortcuts import render

def report_volunteer(request):
    return render(request, 'report_volunteer/index.html')
