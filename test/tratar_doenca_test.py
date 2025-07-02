import pytest
from unittest.mock import Mock, patch
from domain.carta.tratar_doenca import TratarDoenca
from enuns.cor import Cor
from domain.cidade import Cidade
from domain.jogador import Jogador
from domain.doenca import Doenca
from controller.jogo_controller import Jogo # Importar Jogo real para testar get_doenca

@pytest.fixture
def mock_jogo():
    # Mock do Jogo para controlar o estado das doenças
    jogo = Jogo.get_instancia()
    jogo.doencas = {
        Cor.AZUL: Doenca(Cor.AZUL),
        Cor.AMARELO: Doenca(Cor.AMARELO),
        Cor.PRETO: Doenca(Cor.PRETO),
        Cor.VERMELHO: Doenca(Cor.VERMELHO),
    }
    return jogo

@pytest.fixture
def mock_cidade():
    cidade = Cidade("TestCity")
    return cidade

@pytest.fixture
def mock_jogador(mock_cidade):
    jogador = Jogador("TestPlayer", mock_cidade, 1)
    return jogador

def test_tratar_doenca_normal(mock_jogo, mock_cidade, mock_jogador):
    # Cenário: Tratar doença normalmente (sem cura ou centro de pesquisa)
    mock_cidade.adicionar_nivel_doenca(Cor.AZUL, 3)
    mock_jogador.posicao = mock_cidade # Garante que o jogador está na cidade correta

    carta_tratar = TratarDoenca(Cor.AZUL)
    carta_tratar.ativar(mock_jogo, mock_jogador)

    assert mock_cidade.get_nivel_doenca(Cor.AZUL) == 2

def test_tratar_doenca_com_cura_e_centro_pesquisa(mock_jogo, mock_cidade, mock_jogador):
    # Cenário: Tratar doença com cura descoberta e centro de pesquisa
    mock_cidade.adicionar_nivel_doenca(Cor.VERMELHO, 3)
    mock_cidade.construir_centro_pesquisa() # Adiciona centro de pesquisa
    mock_jogador.posicao = mock_cidade # Garante que o jogador está na cidade correta

    # Simula a cura da doença
    mock_jogo.doencas[Cor.VERMELHO].curada = True

    carta_tratar = TratarDoenca(Cor.VERMELHO)
    carta_tratar.ativar(mock_jogo, mock_jogador)

    assert mock_cidade.get_nivel_doenca(Cor.VERMELHO) == 0

def test_tratar_doenca_com_cura_sem_centro_pesquisa(mock_jogo, mock_cidade, mock_jogador):
    # Cenário: Tratar doença com cura descoberta, mas sem centro de pesquisa
    mock_cidade.adicionar_nivel_doenca(Cor.AMARELO, 3)
    mock_jogador.posicao = mock_cidade # Garante que o jogador está na cidade correta

    # Simula a cura da doença
    mock_jogo.doencas[Cor.AMARELO].curada = True

    carta_tratar = TratarDoenca(Cor.AMARELO)
    carta_tratar.ativar(mock_jogo, mock_jogador)

    assert mock_cidade.get_nivel_doenca(Cor.AMARELO) == 2

def test_tratar_doenca_sem_cura_com_centro_pesquisa(mock_jogo, mock_cidade, mock_jogador):
    # Cenário: Tratar doença sem cura descoberta, mas com centro de pesquisa
    mock_cidade.adicionar_nivel_doenca(Cor.PRETO, 3)
    mock_cidade.construir_centro_pesquisa() # Adiciona centro de pesquisa
    mock_jogador.posicao = mock_cidade # Garante que o jogador está na cidade correta

    carta_tratar = TratarDoenca(Cor.PRETO)
    carta_tratar.ativar(mock_jogo, mock_jogador)

    assert mock_cidade.get_nivel_doenca(Cor.PRETO) == 2
