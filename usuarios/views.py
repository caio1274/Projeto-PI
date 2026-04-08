from django.shortcuts import render, redirect
from django.http import HttpRequest
from .dados import Dados
from .models import Usuarios
from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings


def carregando(request):
    return render(request, 'Projeto-PI/html/carregando.html')


def index(request):
    return render(request, 'Projeto-PI/index.html')


def navegacao(request):
    return render(request, 'Projeto-PI/html/navegacao.html')


def acessar(request):
    return render(request, 'Projeto-PI/html/acesso.html')


def login(request: HttpRequest):
    formulario = Dados()
    contexto = {'form': formulario}
    return render(request, 'Projeto-PI/html/login.html', contexto)


def acessarIA(request):
    return render(request, 'Projeto-PI/html/liaia.html')

def entrar(request):
    if request.method == "POST":

        email = request.POST.get("email")
        senha = request.POST.get("senha")

        try:
            usuario = Usuarios.objects.get(email=email)

            senha_com_pepper = senha + settings.PASSWORD_PEPPER

            if check_password(senha_com_pepper, usuario.senha):

                request.session["usuario_id"] = usuario.id
                return redirect("liaia")

            else:
                return redirect("login")

        except Usuarios.DoesNotExist:
            return redirect("login")

    return render(request, "Projeto-PI/html/login.html")

def cadastro(request):

    if request.method == "POST":

        formulario = Dados(request.POST)

        if formulario.is_valid():

            senha = request.POST.get("senha")   

            usuario = formulario.save(commit=False)
            senha_com_pepper = senha + settings.PASSWORD_PEPPER

            usuario.senha = make_password(senha_com_pepper)
            usuario.save()

            return redirect("login")

    else:
        formulario = Dados()

    return render(
        request,
        "Projeto-PI/html/cadastro.html",
        {"form": formulario}
    )


def jogos(request):
    return render(request, 'Projeto-PI/html/jogos.html')


def exercicios(request):
    return render(request, 'Projeto-PI/html/exercicios.html')