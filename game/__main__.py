# imports internos
from game.objects import Jogador, Menu, Jogo
from game.utils.terminal import cls, pause, finalizar_programa


# imports externos


def main():
    menu: Menu = Menu()
    cls()
    menu.exibir_regras()
    pause()
    try:
        while True:
            cls()
            menu.exibir_menu()
            opcao: str = menu.ler_opcao()
            match opcao:
                case '1':
                    jogo: Jogo = Jogo()
                    cls()
                    jogo.adicionar_jogador()
                    cls()
                    jogo.adicionar_jogador()
                    while not jogo.verificar_vencedor():
                        cls()
                        jogo.turno()
                        pause()
                        jogo.trocar_turno()
                    pause()
                    continue
                case '2':
                    cls()
                    menu.exibir_regras()
                    pause()
                case '3':
                    finalizar_programa()
    except KeyboardInterrupt:
        finalizar_programa()
        

if __name__ == "__main__":
    main()
