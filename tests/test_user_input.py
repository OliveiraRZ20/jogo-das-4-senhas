import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# imports internos
from game.utils.validator import validar_nome, validar_tentativa, validar_palavra

# imports externos
import pytest

class TestValidator:
    """Testes para as funções de validação de entrada de usuário."""
    
    def test_validar_nome_valido(self):
        """Teste para nome válido."""
        resultado, mensagem = validar_nome("Lucca")
        assert resultado is True
        assert mensagem == ""
    
    def test_validar_nome_vazio(self):
        """Teste para nome vazio."""
        resultado, mensagem = validar_nome("")
        assert resultado is False
        assert mensagem == "Nome inválido! O nome não pode ser vazio. Tente novamente."
    
    def test_validar_nome_com_numeros(self):
        """Teste para nome com números."""
        resultado, mensagem = validar_nome("Lucca123")
        assert resultado is False
        assert mensagem == "Nome inválido! Apenas letras são permitidas. Tente novamente."
    
    def test_validar_tentativa_valida(self):
        """Teste para tentativa válida."""
        resultado, mensagem = validar_tentativa("ABCDEF")
        assert resultado is True
        assert mensagem == ""
    
    def test_validar_tentativa_vazia(self):
        """Teste para tentativa vazia."""
        resultado, mensagem = validar_tentativa("")
        assert resultado is False
        assert mensagem == "Tentativa inválida! A tentativa não pode ser vazia. Tente novamente."
    
    def test_validar_tentativa_com_caracteres_invalidos(self):
        """Teste para tentativa com caracteres inválidos."""
        resultado, mensagem = validar_tentativa("ABCD1E")
        assert resultado is False
        assert mensagem == "Tentativa inválida! Apenas letras são permitidas. Tente novamente."
    
    def test_validar_palavra_valida(self):
        """Teste para palavra válida."""
        palavras_existentes = ["CASARAO", "CARRO"]
        resultado, mensagem = validar_palavra("FLORESTA", palavras_existentes)
        assert resultado is True
        assert mensagem == ""
    
    def test_validar_palavra_comprimento_invalido(self):
        """Teste para palavra com comprimento inválido."""
        palavras_existentes = []
        resultado, mensagem = validar_palavra("CAR", palavras_existentes)
        assert resultado is False
        assert mensagem == "Palavra inválida! A palavra deve ter entre 5 e 15 letras. Tente novamente."
    
    def test_validar_palavra_ja_existente(self):
        """Teste para palavra já existente."""
        palavras_existentes = ["CASARAO", "CARRO"]
        resultado, mensagem = validar_palavra("CASARAO", palavras_existentes)
        assert resultado is False
        assert mensagem == "Palavra inválida! Você já adicionou essa palavra antes. Tente novamente."
    
    def test_validar_palavra_com_caracteres_invalidos(self):
        """Teste para palavra com caracteres inválidos."""
        palavras_existentes = []
        resultado, mensagem = validar_palavra("FLORESTA1", palavras_existentes)
        assert resultado is False
        assert mensagem == "Palavra inválida! Apenas letras são permitidas. Tente novamente."