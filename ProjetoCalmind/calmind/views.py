from django.shortcuts import render

def carregando(request):
    return render(request, 'carregando.html')

def index(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def chat(request):
    return render(request, 'chat.html')

def navegacao(request):
    return render(request, 'navegacao.html')

def jogos(request):
    return render(request, 'jogos.html')