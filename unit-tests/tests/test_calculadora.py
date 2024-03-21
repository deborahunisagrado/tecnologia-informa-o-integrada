from exercicios.calculadora import adicao, subtracao, multiplicacao, divisao
import pytest

def test_soma():
    assert adicao(1, 2) == 3
    assert adicao(-1, 2) == 1
    assert adicao(0, 0) == 0

def test_subtracao():
    assert subtracao(5, 2) == 3
    assert subtracao(-1, -1) == 0
    assert subtracao(10, 7) == 3

def test_multiplicacao():
    assert multiplicacao(2, 3) == 6
    assert multiplicacao(-2, 3) == -6
    assert multiplicacao(0, 5) == 0

def test_divisao():
    assert divisao(6, 3) == 2
    assert divisao(10, 2) == 5
    assert divisao(5, 2) == 2.5

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(10, 0)

def test_tipo_invalido():
    with pytest.raises(TypeError):
        adicao(5, "2")

    with pytest.raises(TypeError):
        subtracao("5", 2)

    with pytest.raises(TypeError):
        multiplicacao(3, "a")

    with pytest.raises(TypeError):
        divisao("10", 2)
        