import pytest
from domain.cidade import Cidade

def test_adicionar_vizinha():
    c1 = Cidade('Rio de Janeiro')
    c2 = Cidade('São Paulo')
    c3 = Cidade('Baia')

    c1.adicionar_vizinha(c2)
    assert c2 in c1.vizinhas
    assert c1 in c2.vizinhas

    c2.adicionar_vizinha(c3)
    assert c3 in c2.vizinhas
    assert c2 in c3.vizinhas

    assert len(c1.vizinhas) == 1
    assert len(c2.vizinhas) == 2
    assert len(c3.vizinhas) == 1

def test_centro_pesquisa():
    cidade = Cidade('Belo Horizonte')
    assert not cidade.tem_centro_pesquisa
    cidade.construir_centro_pesquisa()
    assert cidade.tem_centro_pesquisa
