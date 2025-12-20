# imports internos
from game.utils.user_input import ler_opcao


# imports externos


REGRAS: str = """
|+---------------------------------------------------------------------------------+|
|                                    REGRAS                                         |
|+---------------------------------------------------------------------------------+|
| - O jogo consiste em 2 jogadores que irão definir 4 palavras cada um.             |
| - Cada palavra deve ter entre 5 a 15 letras.                                      |
| - Cada palavra subsequente deve ter relação com a palavra anterior.               |
| - Os jogadores irão se revezar tentando descobrir as palavras do adversário.      |
| - A cada rodada, o jogador deve tentar adivinhar a palavra atual do adversário.   |
| - Em caso de erro, uma letra da palavra será revelada para ajudar na adivinhação. |
| - Em caso de acerto, o jogador avança para a próxima palavra.                     |
| - O jogo termina quando um jogador descobre todas as palavras do adversário.      |
|+---------------------------------------------------------------------------------+|
"""

MENU: str = """
|+-----------------------------+|
|             MENU              |
|+-----------------------------+|
| 1. Iniciar um novo jogo       |
| 2. Ver as regras do jogo      |
| 3. Sair do jogo               |
|+-----------------------------+|
"""

class Menu:
    
    @staticmethod
    def exibir_regras():
        print(REGRAS)
    
    @staticmethod
    def exibir_menu():
        print(MENU)
    
    @staticmethod
    def ler_opcao() -> str:
        escolha: str = ler_opcao("Escolha uma opção (1-3):\n> ", ['1', '2', '3'])
        return escolha

