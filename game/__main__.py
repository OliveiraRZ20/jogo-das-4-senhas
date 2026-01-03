# imports internos
from game.objects import Jogador, Menu, Jogo
from game.utils.terminal import cls, pause, finalizar_programa
from game.utils.user_input import ler_nome, ler_opcao, definir_palavras
from game.utils.logger import alertar, informar, confirmar

# imports externos

def inciar_partida():
    jogo: Jogo = Jogo()
    cls()
    
    for _ in range(2):
        cls()
        jogo.adicionar_jogador(Jogador(ler_nome(), definir_palavras()))
    
    while True:
        cls()
        jogo.turno()
        
        resultado, mensagem = jogo.verificar_vencedor()
        match resultado:
            case True:
                confirmar(mensagem)
                pause()
                break
            case False:
                pause()
                jogo.trocar_turno()

def main():
    menu: Menu = Menu()
    cls()
    menu.exibir_regras()
    pause()
    try:
        while True:
            cls()
            menu.exibir_menu()
            opcao: str = ler_opcao("Escolha uma opção (1-3):\n> ", ['1', '2', '3'])
            match opcao:
                case '1':
                    inciar_partida()
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
