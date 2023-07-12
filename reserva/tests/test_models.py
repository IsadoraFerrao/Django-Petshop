from datetime import date
import pytest
from model_bakery import baker
from reserva.models import Reserva, Petshop

@pytest.fixture
def reserva():
    reserva = baker.make(
        Reserva,
        nome='Tom',
        data=date.today(),
        turno='Tarde'
    )
    return reserva

@pytest.mark.django_db
def test_str_reserve_deve_retornar_string_formatada(reserva):
    assert str(reserva) == 'Tom: 2023-07-12 - Tarde' #alterar esse teste pra data atual
    
"""
@pytest.mark.django_db
def test_str_reserve_deve_retornar_string_formatada():
    reserva = baker.make(
        Reserva,
        nome='Tom',
        data=date.today(),
        turno='Tarde'
    )
    assert str(reserva) == 'Tom: 2023-07-12 - Tarde' #alterar esse teste pra data atual
"""


"""@pytest.mark.django_db
def test_petshop_qtd_reserva_deve_retornanr_numero_reservas(petshop):
    petshop = baker.make(Petshop)
    quantidade = 3
    baker.make(
        Reserva, 
        quantidade, 
        petshop=petshop
    )

    assert petshop.qtd_reserva() == 3
"""