import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# imports internos
from game.objects import Jogador

# imports externos
import pytest

@pytest.fixture
def jogador():
    """Fixture para criar um jogador de teste."""
    return Jogador()


class TestJogador:
    """Testes para a classe Jogador."""
    
    def test_inicializacao(self, jogador):
        """Teste para a inicialização do jogador."""
        assert jogador.nome == ''
        assert jogador.palavras == []
        assert jogador.pontos == 0
        assert jogador.qtd_letras_descobertas == 0
    
    def test_definir_nome(self, jogador):
        """Teste para o método definir_nome."""
        novo_nome = "Lucca"
        jogador.definir_nome(novo_nome)
        assert jogador.nome == novo_nome

    def test_definir_palavras(self, jogador):
        """Teste para o método definir_palavras."""
        novas_palavras = ["casa", "carro", "floresta", "computador"]
        jogador.definir_palavras(novas_palavras)
        assert jogador.palavras == novas_palavras
    
    def test_ganhar_letra(self, jogador):
        """Teste para o método ganhar_letra."""
        jogador.ganhar_letra()
        assert jogador.qtd_letras_descobertas == 1
        jogador.ganhar_letra()
        assert jogador.qtd_letras_descobertas == 2
    
    def test_pontuar(self, jogador):
        """Teste para o método pontuar."""
        jogador.ganhar_letra()
        jogador.pontuar()
        assert jogador.pontos == 1
        assert jogador.qtd_letras_descobertas == 0
        jogador.ganhar_letra()
        jogador.pontuar()
        assert jogador.pontos == 2
        assert jogador.qtd_letras_descobertas == 0