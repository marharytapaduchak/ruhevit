from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.profile_page, name='profile_page'),
    path(
        'logout/',
        LogoutView.as_view(next_page='/accounts/login/'),
        name='logout'
    ),
    path('requests/', include('requests.urls')),
]
