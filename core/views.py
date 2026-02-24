from django.shortcuts import render
from django.shortcuts import redirect

def carregando(request):
    return render(request, 'Projeto-PI/html/carregando.html')

def index(request):
    return render(request, 'Projeto-PI/index.html')

def navegacao(request):
    return render(request, 'Projeto-PI/html/navegacao.html')

def acessar(request):
    return render(request,'Projeto-PI/html/acesso.html')

def login(request):
    return render(request,'Projeto-PI/html/login.html')
def acessarIA(request):
    return render(request,'Projeto-PI/html/liaia.html')

def entrar(request):
    return redirect('acessarIA')  # nome da rota da LiaIA

def cadastro(request):
    return render(request,'Projeto-PI/html/cadastro.html')

from django.shortcuts import render

def jogos(request):
    return render(request, 'Projeto-PI/html/jogos.html')


def exercicios(request):
    return render(request, 'Projeto-PI/html/exercicios.html')