from exercicios.validar_senha import validate_password

def test_validate_password():
    # Senha válida
    assert validate_password("Senha1@") == "Senha validada"

    # Senhas inválidas
    assert validate_password("senha") == ["Tamanho mínimo de caracteres: 6",
                                         "É necessário conter pelo menos 1 letra(s) maiúscula(s)",
                                         "É necessário conter pelo menos 1 número(s)",
                                         "É necessário conter pelo menos 1 caracter(es) especial(is) '@#$'"]

    assert validate_password("senha123") == ["É necessário conter pelo menos 1 letra(s) maiúscula(s)",
                                             "É necessário conter pelo menos 1 caracter(es) especial(is) '@#$'"]

    assert validate_password("SENHA123") == ["É necessário conter pelo menos 1 letra(s) minúscula(s)",
                                             "É necessário conter pelo menos 1 caracter(es) especial(is) '@#$'"]

    assert validate_password("SENHA@") == ["É necessário conter pelo menos 1 letra(s) minúscula(s)",
                                           "É necessário conter pelo menos 1 número(s)"]

    assert validate_password("senha123@") == ["É necessário conter pelo menos 1 letra(s) maiúscula(s)"]