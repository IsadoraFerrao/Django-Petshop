import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_todos_petshops():
    cliente = APIClient()
    resposta = cliente.get('/api/petshop')
    assert len(resposta.data['results']) == 0
