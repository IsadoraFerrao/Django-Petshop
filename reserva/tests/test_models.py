from datetime import date
import pytest
from model_bakery import baker
from reserva.models import Reserva

# def __str__(self):
    # return f'{self.nome}: {self.data} - {self.turno}'

#FIXTURE
@pytest.fixture
def reserva():
    reserva = baker.make(
        Reserva,
        nome = 'Tom',
        data=date.today(),
        turno = 'Tarde'
    )
    return reserva

@pytest.mark.django_db
def test_reserva_deve_retornar_string_formata(reserva):
    assert str(reserva) == 'Tom: 2023-07-18 - Tarde'

