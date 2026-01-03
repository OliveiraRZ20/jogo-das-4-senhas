# imports internos
from game.utils.logger import alertar, informar, confirmar
from game.utils.validator import validar_nome, validar_palavra, validar_tentativa


# imports externos


def ler_opcao(input_message: str, opcoes_validas: list[str]) -> str:
    """Função genérica para leitura de uma opção dentre as opções válidas fornecidas"""
    while True:
        opcao: str = input(input_message).strip()
        if opcao not in opcoes_validas:
            alertar("Opção inválida! Tente novamente.")
        else:
            return opcao


def ler_nome() -> str:
    """Função para leitura do nome do jogador no momento da criação do jogador"""
    while True:
        nome: str = input("Digite o nome do jogador:\n> ").strip().capitalize()
        resultado, mensagem = validar_nome(nome)
        match resultado:
            case True:
                return nome
            case False:
                alertar(mensagem)


def ler_tentativa(input_message: str) -> str:
    """Função para leitura da tentativa do jogador durante o seu turno"""
    while True:
        tentativa: str = input(input_message).strip().upper()
        resultado, mensagem = validar_tentativa(tentativa)
        match resultado:
            case True:
                return tentativa
            case False:
                alertar(mensagem)

def ler_palavra(input_message: str, palavras_existentes: list[str]) -> str:
    """Função para leitura de uma palavra no momento de definição das palavras do jogador ao inciar o jogo"""
    while True:
        palavra: str = input(input_message).strip().upper()
        resultado, mensagem = validar_palavra(palavra, palavras_existentes)
        match resultado:
            case True:
                return palavra
            case False:
                alertar(mensagem)

def definir_palavras() -> list[str]:
    informar(f"agora você irá definir suas 4 palavras secretas, não deixe o outro jogador ver!")
    palavras: list[str] = []
    for i in range(4):
        if i == 0:
            input_message: str = f"digite a primeira palavra que deseja adicionar:\n> "
        else:
            input_message: str = f"digite uma palavra que tenha a ver com a palavra anterior ({palavras[i-1]}):\n> "
        palavra: str = ler_palavra(input_message, palavras)
        palavras.append(palavra)
    return palavras
