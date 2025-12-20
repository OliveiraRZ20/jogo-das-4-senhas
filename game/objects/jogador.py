# imports internos
from game.utils.logger import informar
from game.utils.user_input import ler_palavra, ler_nome

# imports externos


class Jogador():
    def __init__(self):
        self.nome: str = ''
        self.palavras: list[str] = []
        self.pontos: int = 0
        self.qtd_letras_descobertas: int = 0
    
    def definir_nome(self):
        self.nome = ler_nome("Digite o nome do jogador:\n> ")
    
    def definir_palavras(self):
        informar(f"{self.nome}, agora você irá definir suas 4 palavras secretas, não deixe o outro jogador ver!")
        for i in range(4):
            if i == 0:
                input_message: str = f"{self.nome}, digite a primeira palavra que deseja adicionar:\n> "
            else:
                input_message: str = f"{self.nome}, digite uma palavra que tenha a ver com a palavra anterior ({self.palavras[i-1]}):\n> "
            palavra: str = ler_palavra(input_message, self.palavras)
            self.palavras.append(palavra)
    
    def pontuar(self):
        self.pontos += 1
        self.qtd_letras_descobertas = 0

