from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

@login_required
def changing_info(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # Після збереження можна перенаправити на сторінку профілю або показати повідомлення
            return redirect('profile_page')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'changing_info/index.html', {'form': form})
