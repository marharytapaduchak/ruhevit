from django.urls import path
from . import views

urlpatterns = [
    path('', views.errors, name='errors'),
]
