from exercicios.contar_palavras import contar_palavras

def test_contar_palavras():
    texto1 = "Isso é um texto de exemplo."
    texto2 = "Esta é uma frase com um número diferente de palavras."
    texto3 = "Palavras, palavras e mais palavras."

    assert contar_palavras(texto1) == 6
    assert contar_palavras(texto2) == 8
    assert contar_palavras(texto3) == 6