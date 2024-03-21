from exercicios.lista import ordenar_crescente, ordenar_decrescente

def test_ordenar_crescente():
    assert ordenar_crescente([1, 3, 2, 5, 4]) == [1, 2, 3, 4, 5]
    assert ordenar_crescente([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert ordenar_crescente([5, 2, 4, 1, 3]) == [1, 2, 3, 4, 5]

def test_ordenar_decrescente():
    assert ordenar_decrescente([1, 3, 2, 5, 4]) == [5, 4, 3, 2, 1]
    assert ordenar_decrescente([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]
    assert ordenar_decrescente([5, 2, 4, 1, 3]) == [5, 4, 3, 2, 1]