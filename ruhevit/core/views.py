from django.shortcuts import render

def home_redirect(request):
    if request.user.is_authenticated:
        return render(request, 'home/index.html')
    else:
        return render(request, 'landing/index.html')


def custom_404_view(request, exception):
    return render(request, 'errors/404.html', status=404)
