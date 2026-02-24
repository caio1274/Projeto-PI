from django.urls import path
from . import views

urlpatterns = [
    path('', views.carregando, name='carregando'),  # primeira página
    path('index/', views.index, name='index'),
    path('acesso/', views.acessar, name='acesso'),
    path('navegacao/', views.navegacao, name='navegacao'),
    path('login/', views.login, name='login'),
    path('LiaIA/', views.acessarIA, name='liaia'),
    path('entrar/', views.entrar, name='entrar'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('jogos/', views.jogos, name='jogos'),
    path('exercicios/', views.exercicios, name='exercicios'),
]