from colorama import Fore, Style, init

# Inicializa colorama (crucial para Windows)
init(autoreset=True)

def alertar(msg: str) -> None:
    """Exibe uma mensagem de alerta no terminal na cor VERMELHA."""
    print(f"{Fore.RED}[ERRO] {msg}{Style.RESET_ALL}")

def informar(msg: str) -> None:
    """Exibe uma mensagem informativa no terminal na cor AMARELA."""
    print(f"{Fore.YELLOW}[INFO] {msg}{Style.RESET_ALL}")

def confirmar(msg: str) -> None:
    """Exibe uma mensagem de confirmação no terminal na cor VERDE."""
    print(f"{Fore.GREEN}[SUCESSO] {msg}{Style.RESET_ALL}")