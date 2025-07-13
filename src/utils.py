from os import system

mensagem_bem_vindo: str = """
| ============================================================== |
|                 Bem-vindo ao jogo das 4 senhas                 |
| ============================================================== |
| Instruções:                                                    |
| - Você e seu oponente escolherão 4 palavras.                   |
| - Cada palavra deve estar relacionada à anterior.              |
| - O jogo é jogado em turnos.                                   |
| - Em cada turno, você tenta adivinhar a palavra do adversário. | 
| - Se acertar, avança para a próxima palavra.                   |
| - Se errar, ganha uma letra da palavra e passa a vez.          |
| - O jogo termina quando um jogador adivinhar todas as palavras.|
| ============================================================== |
"""

class Utils:
    @staticmethod
    def limpar_tela() -> None:
        system("cls")
        return

    @staticmethod
    def mostrar_mensagem_bem_vindo() -> None:
        print(mensagem_bem_vindo)
        return
    
    @staticmethod
    def validar_nome(nome: str) -> bool:
        if not nome:
            print("O nome não pode ser vazio. Tente novamente.")
            return False
        elif len(nome) > 20:
            print("O nome não pode ter mais de 20 caracteres. Tente novamente.")
            return False
        elif nome not in "abcdefghijklmnopqrstuvwxyz ":
            print("O nome deve conter apenas letras. Tente novamente.")
            return False
        return True
    
    @staticmethod
    def capturar_nome_validado() -> str:
        while True:
            nome: str = input("Digite o nome do jogador:\n> ").strip().lower()
            if Utils.validar_nome(nome):
                return nome

    @staticmethod
    def validar_palavras(palavras: list[str]) -> bool:
        # verifica lista vazia
        if not palavras:
            print("ERRO: lista vazia, tente novamente.")
            return False
        # verifica lista com número inválido de palavras
        elif len(palavras) < 4 or len(palavras) > 4:
            print(f"ERRO: número inválido de palavras, deve ser 4, tem {len(palavras)}.")
            return False
        # verifica por palavras repetidas
        elif len(set(palavras)) != len(palavras):
            print("ERRO: palavras repetidas, tente novamente.")
            return False
        # verifica se todas as palavras são válidas
        elif not all(palavra.isalpha() for palavra in palavras):
            print("ERRO: todas as palavras devem conter apenas letras. Tente novamente.")
            return False
        # verifica se todas as palavras têm tamanho válido
        elif not all(2 <= len(palavra) <= 20 for palavra in palavras):
            print("ERRO: todas as palavras devem ter entre 2 e 20 letras. Tente novamente.")
            return False
        # verifica se todas as palavras não tem espaços ou hífens
        elif any(" " in palavra or "-" in palavra for palavra in palavras):
            print("ERRO: as palavras não podem conter espaços ou hífens. Tente novamente.")
            return False
        return True
    
    @staticmethod
    def capturar_palavras_validadas() -> list[str]:
        while True:
            palavras: list[str] = input("Digite as palavras do jogador (separadas por espaço):\n> ").strip().lower().split(" ")
            if Utils.validar_palavras(palavras):
                return palavras