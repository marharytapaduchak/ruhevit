from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.changing_info, name='changing_info'),
    path('accounts/password_reset/', RedirectView.as_view(url='/accounts/password_reset/')),
]
