from django import views
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
 path('', views.index, name='index'),
 path('admin-galery/', views.admin, name='admin-galery'),
 path('admin-galery/editar/<str:id>', views.editar, name='editar'),
 path('admin-galery/eliminar/<str:id>', views.eliminar, name='eliminar'),
 path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html',next_page='admin-galery')),
 path('accounts/logout/',auth_views.LogoutView.as_view(next_page='index')),
]