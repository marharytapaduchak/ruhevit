from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth, name='auth'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('reset_pass/', views.reset_pass, name='reset_pass'),
    path('reset_pass_confirm/', views.reset_pass_confirm, name='reset_pass_confirm'),
]
