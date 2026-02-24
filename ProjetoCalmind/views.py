from django.shortcuts import render

def carregando(request):
    return render(request, 'Projeto-PI/html/carregando.html')

def index(request):
    return render(request, 'Projeto-PI/index.html')