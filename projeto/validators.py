import re

def nome_valido (nome):
    return nome.isalpha()

def cidade_valida (cidade):
        return cidade.isalpha()

def telefone_valido (telefone):
        modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
        resposta = re.findall(modelo, telefone)
        return resposta 

def nome_pet_valido (nome_pet):
    return nome_pet.isalpha()

def raca_valido (raca):
    return raca.isalpha()

def especie_valido (especie):
    return especie.isalpha()

def personalidade_valido (personalidade):
    return personalidade.isalpha()

def sobre_pet_valido (sobre_pet):
    return sobre_pet.isalpha()

def porte_valido (porte):
    return porte.isalpha()

def cidade_pet_valido (cidade_pet):
    return cidade_pet.isalpha()
       