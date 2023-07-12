from pytest_django.asserts import assertTemplateUsed

def test_reserva_view_deve_retornar_template(client):
    response = client.get('/reserva/criar/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'criar_reserva.html')