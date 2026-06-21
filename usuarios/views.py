from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from .dados import Dados
from .models import Usuarios

from django.contrib.auth.hashers import make_password, check_password

import json
import ollama


# -----------------------
# PÁGINAS
# -----------------------

def carregando(request):
    return render(request, 'Projeto-PI/html/carregando.html')


def index(request):
    return render(request, 'Projeto-PI/index.html')


def navegacao(request):
    return render(request, 'Projeto-PI/html/navegacao.html')


def acessar(request):
    return render(request, 'Projeto-PI/html/acesso.html')


def acessarIA(request):
    return render(request, 'Projeto-PI/html/liaia.html')


def login(request: HttpRequest):
    formulario = Dados()
    return render(request, 'Projeto-PI/html/login.html', {'form': formulario})


def jogos(request):
    return render(request, 'Projeto-PI/html/jogos.html')


def exercicios(request):
    return render(request, 'Projeto-PI/html/exercicios.html')


# -----------------------
# CADASTRO
# -----------------------

def cadastro(request: HttpRequest):
    if request.method == "POST":
        formulario = Dados(request.POST)

        if formulario.is_valid():
            usuario = formulario.save(commit=False)

            senha = formulario.cleaned_data.get("senha")

            if not senha:
                return redirect("cadastro")

            # PEPPER + HASH (CORRETO)
            senha_com_pepper = senha + settings.PASSWORD_PEPPER
            usuario.senha = make_password(senha_com_pepper)

            usuario.save()

            return redirect("login")

    else:
        formulario = Dados()

    return render(request, 'Projeto-PI/html/cadastro.html', {'form': formulario})


# -----------------------
# LOGIN
# -----------------------

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

    return render(request, 'Projeto-PI/html/login.html')


# -----------------------
# IA (OLLAMA)
# -----------------------

@csrf_exempt
def chat_api(request):
    if request.method == "POST":

        data = json.loads(request.body.decode("utf-8"))
        mensagem = data.get("message")

        resposta = ollama.chat(
            model="llama3",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Você é a LiaIA, uma assistente virtual brasileira. "
                        "Responda SEMPRE em português do Brasil. "
                        "Nunca use inglês."
                    )
                },
                {
                    "role": "user",
                    "content": mensagem
                }
            ]
        )

        return JsonResponse({
            "reply": resposta["message"]["content"]
        })