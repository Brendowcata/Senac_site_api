import re

def telephone_isValid(telephone):
    """Check if the Telephone is valid / Verifica se o Telefone é válido"""
    if telephone == "":
        return True
    standard = '\([0-9]{2}\) [0-9]{4}-[0-9]{4}'
    response = re.findall(standard, telephone)
    return response

       
def phone_number_isValid(phone_number):
    """Check if the Phone_number is valid / Verifica se o número de celular é válido"""
    standard = '\([0-9]{2}\) [0-9]{5}-[0-9]{4}'
    response = re.findall(standard, phone_number)
    return response

def zip_code_isValid(zip_code):
    """Check if the Zip code is valid / Verifica se o CEP é válido"""
    standard = '[0-9]{5}-[0-9]{3}'
    response = re.findall(standard, zip_code)
    return response

def house_number_isValid(house_number):
    """Check if the house number is valid / Verifica se o número do local é válido"""
    return house_number.isnumeric()