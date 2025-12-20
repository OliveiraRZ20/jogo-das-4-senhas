# imports internos
from game.utils.logger import alertar, informar, confirmar

# imports externos
from string import ascii_uppercase

def ler_palavra(input_message: str, palavras_existentes: list[str]) -> str:
    """Função para leitura de uma palavra no momento de definição das palavras do jogador ao inciar o jogo"""
    while True:
        palavra: str = input(input_message).strip().upper()
        if 5 > len(palavra) > 15:
            alertar("Palavra inválida! A palavra deve ter entre 5 e 15 letras. Tente novamente.")
        elif palavra in palavras_existentes:
            alertar("Palavra inválida! Você já adicionou essa palavra antes. Tente novamente.")
        elif any(not char in ascii_uppercase for char in palavra):
            alertar("Palavra inválida! Apenas letras são permitidas. Tente novamente.")
        else:
            return palavra

def ler_nome(input_message: str) -> str:
    """Função para leitura do nome do jogador no momento da criação do jogador"""
    while True:
        nome: str = input(input_message).strip().capitalize()
        if nome == '':
            alertar("Nome inválido! O nome não pode ser vazio. Tente novamente.")
        elif any(not char.upper() in ascii_uppercase for char in nome):
            alertar("Nome inválido! Apenas letras são permitidas. Tente novamente.")
        else:
            return nome

def ler_opcao(input_message: str, opcoes_validas: list[str]) -> str:
    """Função genérica para leitura de uma opção dentre as opções válidas fornecidas"""
    while True:
        opcao: str = input(input_message).strip()
        if opcao not in opcoes_validas:
            alertar("Opção inválida! Tente novamente.")
        else:
            return opcao

def ler_tentativa(input_message: str) -> str:
    """Função para leitura da tentativa do jogador durante o seu turno"""
    while True:
        tentativa: str = input(input_message).strip().upper()
        if tentativa == '':
            alertar("Tentativa inválida! A tentativa não pode ser vazia. Tente novamente.")
        elif any(not char in ascii_uppercase for char in tentativa):
            alertar("Tentativa inválida! Apenas letras são permitidas. Tente novamente.")
        else:
            return tentativa

