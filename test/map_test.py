import pytest
from controller.game_map_controller import GameMap

def test_map_creation():
    game_map = GameMap()
    mapa = game_map.getMap()

    assert len(mapa) == 5 # Assuming NUM_CIDADES is 5

    # Teste de conexão: verificar se todas as cidades têm pelo menos um vizinho
    for cidade in mapa:
        assert len(cidade.vizinhas) > 0, f"Cidade {cidade.nome} não tem vizinhos!"
    
    # Teste de unicidade: verificar se não há cidades duplicadas no mapa
    nomes_cidades = [cidade.nome for cidade in mapa]
    assert len(nomes_cidades) == len(set(nomes_cidades)), "Cidades duplicadas encontradas no mapa!"

    # Teste de bidirecionalidade: verificar se as conexões são bidirecionais
    for cidade in mapa:
        for vizinha in cidade.vizinhas:
            assert cidade in vizinha.vizinhas, \
                f"Conexão unidirecional: {cidade.nome} -> {vizinha.nome}, mas não vice-versa."