from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path('create', views.create_request, name='create_request'),
    path('confirm/<int:request_id>/', views.report_confirm, name='report_confirm'),
    path('view', views.request_view, name='request_view'),
    path('submit/<int:request_id>/', views.report_submit, name='report_submit'),
    path('<int:request_id>/', views.request_detail, name='request_detail'),
    path('requests/<int:request_id>/confirm/',
         views.confirm_request, name='confirm_request'),
]
