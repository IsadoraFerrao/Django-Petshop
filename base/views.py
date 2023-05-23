from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def contato(request):
    contexto = {
        'telefone': '999999',
        'responsavel': 'Maria'
    }
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'contato.html', contexto)