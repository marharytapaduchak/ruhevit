from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from requests.models import Request

@login_required
def index(request):
    # Отримуємо запити, де поточний користувач є власником (військовий створив запит)
    user_requests = Request.objects.filter(owner=request.user).order_by('-created_at')
    
    # Отримуємо "пропозиції допомоги" – запити з статусом "need_volunteer", 
    # але не ті, що створені поточним користувачем
    help_offers = Request.objects.filter(status='need_volunteer').exclude(owner=request.user).order_by('-created_at')
    
    context = {
        'user_requests': user_requests,
        'help_offers': help_offers,
    }
    return render(request, 'home/index.html', context)
