# imports intenos

# imports externos
from string import ascii_uppercase


def validar_nome(nome: str) -> tuple[bool, str]:
    if nome == '':
        return [False, "Nome inválido! O nome não pode ser vazio. Tente novamente."]
    elif any(not char.upper() in ascii_uppercase for char in nome):
        return [False, "Nome inválido! Apenas letras são permitidas. Tente novamente."]
    else:
        return [True, ""]


def validar_tentativa(tentativa: str) -> tuple[bool, str]:
    if tentativa == '':
        return [False, "Tentativa inválida! A tentativa não pode ser vazia. Tente novamente."]
    elif any(not char in ascii_uppercase for char in tentativa):
        return [False, "Tentativa inválida! Apenas letras são permitidas. Tente novamente."]
    else:
        return [True, ""]
    

def validar_palavra(palavra: str, palavras_existentes: list[str]) -> tuple[bool, str]:
    if len(palavra) < 5 or len(palavra) > 15:
        return [False, "Palavra inválida! A palavra deve ter entre 5 e 15 letras. Tente novamente."]
    elif palavra in palavras_existentes:
        return [False, "Palavra inválida! Você já adicionou essa palavra antes. Tente novamente."]
    elif any(not char in ascii_uppercase for char in palavra):
        return [False, "Palavra inválida! Apenas letras são permitidas. Tente novamente."]
    else:
        return [True, ""]
