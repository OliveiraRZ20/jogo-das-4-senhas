class Jogador():
    def __init__(self, nome: str = "", palavras: list[str] = []):
        # nome do jogador
        self.nome: str = nome
        # lista de palavras do jogador (que o adversário deve adivinhar)
        self.palavras: list[str] = palavras
        # index da palavra atual na lista do jogador adversário
        self.progresso: int = 0
        # lista de letras reveladas da palavra atual na lista do jogador adversário
        self.letras_reveladas: list[str] = []
    
    def avancar_progresso(self) -> None:
        self.progresso += 1
        return
    
    def limpar_letras_reveladas(self) -> None:
        self.letras_reveladas.clear()
        return
    
    