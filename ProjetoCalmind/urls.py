from django.contrib import admin
from django.urls import path, include
from . import views
from liaia.chat import chat_api

urlpatterns = [
    path('', include('usuarios.urls')), 
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
        path('chat-api/', chat_api),
]