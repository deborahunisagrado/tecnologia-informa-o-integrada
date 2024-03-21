# test_diferenca_datas.py
from exercicios.datas import calcular_diferenca

def test_calcular_diferenca_dias():
    data1 = '2022-01-01'
    data2 = '2022-01-10'
    assert calcular_diferenca(data1, data2, 'dias') == 9

def test_calcular_diferenca_meses():
    data1 = '2022-01-01'
    data2 = '2023-01-01'
    assert calcular_diferenca(data1, data2, 'meses') == 12

def test_calcular_diferenca_anos():
    data1 = '2022-01-01'
    data2 = '2023-01-01'
    assert calcular_diferenca(data1, data2, 'anos') == 1

def test_calcular_diferenca_horas():
    data1 = '2022-01-01'
    data2 = '2022-01-02'
    assert calcular_diferenca(data1, data2, 'horas') == 24

def test_calcular_diferenca_minutos():
    data1 = '2022-01-01'
    data2 = '2022-01-02'
    assert calcular_diferenca(data1, data2, 'minutos') == 24 * 60
