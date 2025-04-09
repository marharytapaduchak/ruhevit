from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_military, name='report_military'),
]
