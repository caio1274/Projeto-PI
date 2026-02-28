from django.shortcuts import render,redirect
from django.http import HttpRequest
from .dados import Dados
from .models import Usuarios
import hashlib
def carregando(request):
    return render(request, 'Projeto-PI/html/carregando.html')

def index(request):
    return render(request, 'Projeto-PI/index.html')

def navegacao(request):
    return render(request, 'Projeto-PI/html/navegacao.html')

def acessar(request):
    return render(request,'Projeto-PI/html/acesso.html')

def login(request: HttpRequest):
    formulario = Dados()
    contexto = {
        'form': formulario
    }
    return render(request, 'Projeto-PI/html/login.html', contexto)

def acessarIA(request):
    return render(request,'Projeto-PI/html/liaia.html')

def entrar(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        # Criptografa igual no cadastro
        senha = hashlib.sha256(senha.encode()).hexdigest()

        try:
            usuario = Usuarios.objects.get(email=email, senha=senha)
            return redirect('liaia')  # nome da sua página da IA
        except Usuarios.DoesNotExist:
            return redirect('login')

    return render(request, 'login.html')
def cadastro(request: HttpRequest):
    if request.method == "POST":
        formulario = Dados(request.POST)
        if formulario.is_valid():
            senha = formulario.cleaned_data['senha']
            usuario = formulario.save(commit=False)
            usuario.senha = hashlib.sha256(senha.encode()).hexdigest()
            usuario.save()
            return redirect('login')

    else:
        formulario = Dados()

    contexto = {
        'form': formulario
    }

    return render(request, 'Projeto-PI/html/cadastro.html', contexto)

def jogos(request):
    return render(request, 'Projeto-PI/html/jogos.html')

def exercicios(request):
    return render(request, 'Projeto-PI/html/exercicios.html')