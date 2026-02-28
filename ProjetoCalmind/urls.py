from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('usuarios.urls')), 
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
]