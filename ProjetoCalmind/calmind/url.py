from django.urls import path
from . import views

urlpatterns = [
    path('', views.carregando, name='carregando'),
    path('index/', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('chat/', views.chat, name='chat'),
    path('menu/', views.navegacao, name='menu'),
    path('jogos/', views.jogos, name='jogos'),
]