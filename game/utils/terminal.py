# imports internos
from game.utils.logger import confirmar

# imports externos
from os import system, name


def cls():
    """Limpa a tela"""
    system("cls" if name == "nt" else "clear")

def pause():
    """Pausa a execução"""
    input("\nPressione a tecla 'Enter' para continuar...")

def finalizar_programa():
    """Finaliza o programa"""
    print("")
    confirmar("Programa finalizado com sucesso!")
    exit(0)
