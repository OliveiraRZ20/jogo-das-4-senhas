# imports internos
from game.objects import Jogador, Menu, Jogo
from game.utils.terminal import cls, pause, finalizar_programa


# imports externos


def main():
    MENU: Menu = Menu()
    cls()
    MENU.exibir_regras()
    pause()
    try:
        while True:
            cls()
            MENU.exibir_menu()
            opcao: str = MENU.ler_opcao()
            match opcao:
                case '1':
                    JOGO: Jogo = Jogo()
                    cls()
                    JOGO.adicionar_jogador()
                    cls()
                    JOGO.adicionar_jogador()
                    while not JOGO.verificar_vencedor():
                        cls()
                        JOGO.turno()
                        pause()
                        JOGO.trocar_turno()
                    pause()
                    continue
                case '2':
                    cls()
                    MENU.exibir_regras()
                    pause()
                case '3':
                    finalizar_programa()
    except KeyboardInterrupt:
        finalizar_programa()
        

if __name__ == "__main__":
    main()
