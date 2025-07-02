import pytest
from unittest.mock import Mock
from controller.jogo_controller import Jogo
from domain.doenca import Doenca
from enuns.cor import Cor

@pytest.fixture
def jogo_vazio():
    # Reinicia a instância do Jogo para cada teste
    Jogo._instancia = None
    jogo = Jogo.get_instancia()
    # Garante que as doenças são inicializadas para o teste
    jogo.doencas = {
        Cor.AZUL: Doenca(Cor.AZUL),
        Cor.AMARELO: Doenca(Cor.AMARELO),
        Cor.VERMELHO: Doenca(Cor.VERMELHO),
        Cor.VERDE: Doenca(Cor.VERDE),
    }
    return jogo

def test_victory_condition_all_cured(jogo_vazio):
    # Simula todas as doenças curadas
    for cor in Cor:
        jogo_vazio.doencas[cor].curada = True

    jogo_vazio.verificar_condicoes_finais()
    assert jogo_vazio.vitoria == True
    assert jogo_vazio.game_over == True

def test_victory_condition_not_all_cured(jogo_vazio):
    # Simula apenas algumas doenças curadas
    jogo_vazio.doencas[Cor.AZUL].curada = True
    jogo_vazio.doencas[Cor.AMARELO].curada = True

    jogo_vazio.verificar_condicoes_finais()
    assert jogo_vazio.vitoria == False
    assert jogo_vazio.game_over == False

def test_victory_condition_no_diseases_cured(jogo_vazio):
    # Simula nenhuma doença curada
    jogo_vazio.verificar_condicoes_finais()
    assert jogo_vazio.vitoria == False
    assert jogo_vazio.game_over == False
