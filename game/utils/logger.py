def alertar(msg: str) -> None:
    """Exibe uma mensagem de alerta no terminal na cor VERMELHA."""
    print(f"\033[31m[ERRO] {msg}\033[0m")

def informar(msg: str) -> None:
    """Exibe uma mensagem informativa no terminal na cor AMARELA."""
    print(f"\033[33m[INFO] {msg}\033[0m")

def confirmar(msg: str) -> None:
    """Exibe uma mensagem de confirmação no terminal na cor VERDE."""
    print(f"\033[32m[SUCESSO] {msg}\033[0m")