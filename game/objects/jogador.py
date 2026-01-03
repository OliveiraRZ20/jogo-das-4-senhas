# imports internos

# imports externos


class Jogador():
    def __init__(self, nome: str = '', palavras: list[str] = []):
        self.nome: str = nome
        self.palavras: list[str] = palavras
        self.pontos: int = 0
        self.qtd_letras_descobertas: int = 0
    
    def definir_nome(self, nome_digitado: str):
        self.nome = nome_digitado
    
    def definir_palavras(self, palavras_digitadas: list[str]):
        self.palavras = palavras_digitadas
    
    def ganhar_letra(self):
        self.qtd_letras_descobertas += 1
    
    def pontuar(self):
        self.pontos += 1
        self.qtd_letras_descobertas = 0
