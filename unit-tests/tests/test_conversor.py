from exercicios.conversor import real_para_dolar, dolar_para_real, real_para_euro, euro_para_real
import pytest

def test_real_para_dolar():
    assert real_para_dolar(100) == pytest.approx(20.408163265306122)  

def test_dolar_para_real():
    assert dolar_para_real(100) == pytest.approx(490)  

def test_real_para_euro():
    assert real_para_euro(100) == pytest.approx(18.41620626151013)  

def test_euro_para_real():
    assert euro_para_real(100) == pytest.approx(543)  