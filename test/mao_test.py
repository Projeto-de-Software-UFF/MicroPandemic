import pytest
from domain.mao import Mao
from domain.carta.carta import Carta, TipoCarta

def test_adicionar_e_remover_carta():
    mao = Mao()
    carta1 = Carta("Carta 1", TipoCarta.CIDADE)
    carta2 = Carta("Carta 2", TipoCarta.CIDADE)

    assert mao.adicionar_carta(carta1)
    assert len(mao.cartas) == 1
    assert carta1 in mao.cartas

    assert mao.adicionar_carta(carta2)
    assert len(mao.cartas) == 2
    assert carta2 in mao.cartas

    assert mao.remover_carta(carta1)
    assert len(mao.cartas) == 1
    assert carta1 not in mao.cartas

    assert not mao.remover_carta(carta1) # Tentar remover novamente deve falhar

def test_mao_cheia():
    mao = Mao(limite_cartas=2)
    carta1 = Carta("Carta 1", TipoCarta.CIDADE)
    carta2 = Carta("Carta 2", TipoCarta.CIDADE)
    carta3 = Carta("Carta 3", TipoCarta.CIDADE)

    mao.adicionar_carta(carta1)
    mao.adicionar_carta(carta2)
    assert mao.esta_cheia()
    assert not mao.adicionar_carta(carta3) # Não deve adicionar se a mão estiver cheia
    assert len(mao.cartas) == 2

def test_mao_vazia():
    mao = Mao()
    assert len(mao.cartas) == 0
    assert not mao.esta_cheia()
