from django.shortcuts import render
from galeria.models import Fotografia


def index(request): 
    fotografias = Fotografia.objects.all()
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request):
    return render (request, 'galeria/imagem.html')

def imagemICP(request):
    return render (request, 'galeria/ICP.html')

def imagemA1(request):
    return render (request, 'galeria/A1.html')

def imagemA3(request):
    return render (request, 'galeria/A3.html')

def cert(request):
     return render (request, 'galeria/cert.html')

def agenda(request):
    return render (request,'galeria/agenda.html')