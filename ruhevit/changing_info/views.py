from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm


@login_required
def changing_info(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            updated_user = form.save(commit=False)
            if not updated_user.photo:
                updated_user.photo = 'user_photos/blank.png'
            updated_user.save()
            return redirect('profile_page')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'changing_info/index.html', {'form': form})
