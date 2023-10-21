import pytest
from src.main import suma, esMayor, esMenor, dividir, login

def test_suma():
    assert suma(2, 5) == 7

def test_divivir():
    assert dividir(5, 2) == 2.5

def test_esMayor():
    assert esMayor(9, 7)

def test_esMenor():
    assert esMenor(1, 9)

@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (5, 1, 6), (suma(5,9), 2, 16), 
        (9, 1, 10), (6, 3, 9), 
        (23, 7, 30), (15, 5, 20),
        (suma(8,9), 7, 24), (suma(2,3), suma(7,5), 17), 
        (25, 15, suma(25,15)), (suma(24, 6), 9, 39)
    ]
)
def test_sum_params(input_a, input_b, expected):
    assert suma(input_a, input_b) == expected

def test_login_pass():
    login_passes = login('hand.hurt', 'hurt')
    assert login_passes

def test_login_fail():
    login_fails = login('hand', 'hand')
    assert not login_fails 
    # si retorna False entonces pasará la prueba
