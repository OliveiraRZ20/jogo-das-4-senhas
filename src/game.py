from src.player import Jogador
from src.utils import Utils
from os import system

class Jogo:
    def __init__(self):
        # lista de jogadores (armazenará os objetos dos jogadores)
        self.jogadores: list[Jogador] = []
        # index do jogador atual (alternar entre 0 e 1 a cada turno)
        self.turno_atual: int = 0
    
    def adicionar_jogador(self) -> None:
        # define e valida o nome do jogador
        nome: str = Utils.capturar_nome_validado()
        # define e valida a lista de palavras do jogador
        lista_palavras: list[str] = Utils.capturar_palavras_validadas()
        # adiciona esse jogador temporário à lista de jogadores
        self.jogadores.append(Jogador(nome, lista_palavras))
        return None
    
    def trocar_turno(self) -> None:
        # alterna o turno atual entre 0 e 1
        self.turno_atual = 1 - self.turno_atual
        return None
    
    def turno(self) -> None:
        jogador_atual: Jogador = self.jogadores[self.turno_atual]
        jogador_adversario: Jogador = self.jogadores[1 - self.turno_atual]
        
        palavra_alvo: str = jogador_adversario.palavras[jogador_atual.progresso]
        
        print(f"\nÉ a vez de {jogador_atual.nome}!")
        tentativa: str = input(f"Tente adivinhar a palavra do adversário [Dicas: {" ".join(jogador_atual.letras_reveladas)}]:\n> ").strip().lower()
        # se acertar a palavra
        if tentativa == palavra_alvo:
            print(f"\nParabéns, {jogador_atual.nome}! Você acertou a palavra!")
            jogador_atual.avancar_progresso()
            jogador_atual.limpar_letras_reveladas()
        # se não acertar a palavra
        else:
            print(f"\nQue pena, {jogador_atual.nome}! Você errou a palavra.")
            letra_revelada: str = palavra_alvo[len(jogador_atual.letras_reveladas)]
            jogador_atual.letras_reveladas.append(letra_revelada)
            # se a palavra já tiver sido revelada completamente
            if "".join(jogador_atual.letras_reveladas) == palavra_alvo:
                print(f"Todas as letras foram reveladas. A palavra do adversário era: {palavra_alvo}, continuando para a próxima palavra.")
                jogador_atual.avancar_progresso()
                jogador_atual.limpar_letras_reveladas()
            # se não tiver sido revelada completamente
            else:
                print(f"Você ganhou a letra '{letra_revelada}' da palavra do adversário. Tente novamente na próxima vez!")
        system("pause")
        return None

    def verificar_vitoria(self) -> bool:
        for jogador in self.jogadores:
            if jogador.progresso == 4:
                print(f"\n{jogador.nome} venceu o jogo!")
                return True
        return False
        
        
        