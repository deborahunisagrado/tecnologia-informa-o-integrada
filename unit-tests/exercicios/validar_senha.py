import re

def validate_password(password):
    min_number = 1
    min_upper_char = 1
    min_lower_char = 1
    min_special_char = 1
    min_len = 6
    max_len = 16

    errors = []

    if len(password) < min_len:
        errors.append(f"Tamanho mínimo de caracteres: {min_len}")
    if len(password) > max_len:
        errors.append(f"Tamanho máximo de caracteres: {max_len}")
    if len(re.findall(r"[A-Z]", password)) < min_upper_char:
        errors.append(f"É necessário conter pelo menos {min_upper_char} letra(s) maiúscula(s)")
    if len(re.findall(r"[a-z]", password)) < min_lower_char:
        errors.append(f"É necessário conter pelo menos {min_lower_char} letra(s) minúscula(s)")
    if len(re.findall(r"[0-9]", password)) < min_number:
        errors.append(f"É necessário conter pelo menos {min_number} número(s)")
    if len(re.findall(r"[@#$]", password)) < min_special_char:
        errors.append(f"É necessário conter pelo menos {min_special_char} caracter(es) especial(is) '@#$'")

    if errors:
        return errors
    else:
        return "Senha validada"
