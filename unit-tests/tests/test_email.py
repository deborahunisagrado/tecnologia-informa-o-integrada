from exercicios.validar_email import check

def test_check_email():
    assert check("email@example.com") == "Email válido"
    assert check("emailteste@example.com") == "Email válido"
    assert check("user1234@email.com") == "Email válido"
    assert check("usernametag@example.com") == "Email válido"

    assert check("email@example") == "Email inválido"
    assert check("emailexample.com") == "Email inválido"
    assert check("email.example.com") == "Email inválido"
    assert check("email@examplecom") == "Email inválido"
    assert check("@example.com") == "Email inválido"