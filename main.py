from src.utils import Utils
from src.game import Jogo

def main() -> None:
    
    # criar objeto do jogo
    jogo = Jogo()
    
    # adicionar dois jogadores
    for _ in range(2):
        Utils.limpar_tela()
        Utils.mostrar_mensagem_bem_vindo()
        jogo.adicionar_jogador()
    
    # iniciar o jogo
    while not jogo.verificar_vitoria():
        Utils.limpar_tela()
        jogo.turno()
        jogo.trocar_turno()

if __name__ == "__main__":
    main()
