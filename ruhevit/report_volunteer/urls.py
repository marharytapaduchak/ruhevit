from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_volunteer, name='report_volunteer'),
]
