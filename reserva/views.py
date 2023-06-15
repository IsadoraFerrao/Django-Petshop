from django.shortcuts import render
from reserva.forms import ReservaForm
# Create your views here.
def criar_reserva(request):
    sucesso = False   
    form = ReservaForm(request.POST or None)
    if form.is_valid(): 
        sucesso = True
        form.save()
    contexto = {
        'form':form,
        'sucesso': sucesso
    }
    return render(request, 'criar_reserva.html', contexto)
