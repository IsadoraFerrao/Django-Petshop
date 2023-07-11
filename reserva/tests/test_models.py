from datetime import date
import pytest
from model_bakery import baker
from reserva.models import Reserva

@pytest.mark.django_db

def test_str_reserve_deve_retornar_string_formatada():
    data = data('2023, 07, 1')
    reserva = baker.make(
        Reserva,
        nome='Tom',
        data=data,
        turno='Tarde'
    )
    assert str(reserva) == 'Tom: 2023-07-1 - Tarde'