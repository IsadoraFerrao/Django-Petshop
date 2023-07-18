import pytest
from rest_framework.test import APIClient
from reserva.models import Petshop, Reserva
from model_bakery import baker
import datetime 

"""@pytest.fixture
def agendamento():
    return baker.make(Reserva)
    
@pytest.mark.django_db
def test_todos_agendamentos(agendamento):
    client = APIClient()
    response = client.get('/api/agendamento')

    assert len(response.data['results']) == 1
 
"""
   
@pytest.mark.django_db
def test_todos_petshops():
    cliente = APIClient()
    resposta = cliente.get('/api/petshop')
    assert len(resposta.data['results']) == 0

@pytest.fixture
def dados_agendamento():
    hoje = datetime.date.today()
    petshop = baker.make(Petshop)
    return {
        'nome': 'nome teste', 'email': 'emai@email.com',
        'nome_pet': 'pet teste', 'data': hoje, 'turno': 'manhã',
        'tamanho': 0, 'observacoes': '', 'petshop': petshop.pk,
    }

@pytest.fixture
def usuario():
    return baker.make('auth.User')

@pytest.mark.django_db
def test_criar_agendamento(usuario, dados_agendamento):
    cliente = APIClient()
    cliente.force_authenticate(usuario)
    resposta = cliente.post('/api/agendamento', dados_agendamento)
    assert resposta.status_code == 201
    
