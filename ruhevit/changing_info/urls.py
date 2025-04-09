from django.urls import path
from . import views

urlpatterns = [
    path('', views.changing_info, name='changing_info'),
]
