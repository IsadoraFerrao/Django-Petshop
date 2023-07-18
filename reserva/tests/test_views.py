from pytest_django.asserts import assertTemplateUsed
import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from reserva.models import Petshop, Reserva
from rest_api.serializers import PetshopModelSerializer



def test_reserva_view_deve_retornar_template(client):
    response = client.get('/reserva/criar/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'criar_reserva.html')

