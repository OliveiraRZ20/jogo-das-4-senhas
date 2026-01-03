# imports internos
from game.objects import Jogador
from game.utils.logger import confirmar, informar
from game.utils.user_input import ler_tentativa

# imports externos

class Jogo:
    def __init__(self):
        self.jogadores: list[Jogador] = []
        self.turno_atual: int = 0  # Índice do jogador cujo turno é atual
    
    def adicionar_jogador(self, jogador: Jogador):
        self.jogadores.append(jogador)
    
    def trocar_turno(self):
        troca_turno: dict[int, int] = {0: 1, 1: 0}
        self.turno_atual = troca_turno[self.turno_atual]
    
    def turno(self):
        jogador_atual: Jogador = self.jogadores[self.turno_atual]
        jogador_adversario: Jogador = self.jogadores[1 - self.turno_atual]
        
        informar(f"É a vez de {jogador_atual.nome} jogar!")
        
        if jogador_atual.pontos > 0:
            informar(f"Última palavra descoberta: {jogador_adversario.palavras[jogador_atual.pontos - 1]}")
        
        palavra_alvo: str = jogador_adversario.palavras[jogador_atual.pontos]
        informar(f"Palavra atual: {palavra_alvo[0:jogador_atual.qtd_letras_descobertas]}")
        
        tentativa: str = ler_tentativa(f"{jogador_atual.nome}, digite sua tentativa para a palavra atual:\n> ")
        
        if tentativa == palavra_alvo:
            confirmar(f"Parabéns {jogador_atual.nome}! Você descobriu a palavra '{palavra_alvo}'!")
            jogador_atual.pontuar()
        else:
            informar(f"Que pena {jogador_atual.nome}, você não acertou a palavra.")
            if jogador_atual.qtd_letras_descobertas == len(palavra_alvo) - 1:
                informar("Você não conseguiu descobrir a palavra, mas todas as letras já foram reveladas.")
                informar(f"A palavra era: {palavra_alvo}")
                informar("Você avançou para a próxima palavra.")
                jogador_atual.pontuar()
            else:
                jogador_atual.ganhar_letra()
                informar(f"Uma letra da palavra foi revelada para ajudar: {palavra_alvo[jogador_atual.qtd_letras_descobertas - 1]}")

    def verificar_vencedor(self) -> tuple[bool, str]:
        for jogador in self.jogadores:
            if jogador.pontos == 4:
                return [True, f"Parabéns {jogador.nome}! Você venceu o jogo!"]
        return [False, ""]
