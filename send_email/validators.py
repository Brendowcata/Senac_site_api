import re

def phone_number_isValid(phone_number):
    """Check if the Phone_number is valid / Verifica se o número de celular é válido"""
    if phone_number == "":
        return True
    standard = '\([0-9]{2}\) [0-9]{5}-[0-9]{4}'
    response = re.findall(standard, phone_number)
    return response

def name_isValid(name):
    """Check if the name is valid / Verifica se o nome é válido"""
    if any(char.isdigit() for char in name):
        return False
    else:
        return True
