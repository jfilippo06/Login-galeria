from django import views
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
 path('', views.index, name='index'),
 path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html'))
]