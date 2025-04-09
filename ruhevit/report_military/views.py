from django.shortcuts import render

def report_military(request):
    return render(request, 'report_military/index.html')
