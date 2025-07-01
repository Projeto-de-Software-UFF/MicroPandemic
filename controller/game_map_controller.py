import random
from typing import List
from domain.cidade import Cidade
import config

class GameMap:
    def __init__(self, num_cidades: int, max_vizinhos_por_cidade: int):
        self._map: List[Cidade] = []
        self._num_cidades = num_cidades
        self._max_vizinhos_por_cidade = max_vizinhos_por_cidade
        self._criar_mapa()

    def _criar_mapa(self):
        # Lista de capitais brasileiras para nomes de cidades
        CAPITAIS_BRASILEIRAS = [
            "Rio Branco", "Maceió", "Macapá", "Manaus", "Salvador", "Fortaleza", "Brasília",
            "Vitória", "Goiânia", "São Luís", "Cuiabá", "Campo Grande", "Belo Horizonte",
            "Belém", "João Pessoa", "Curitiba", "Recife", "Teresina", "Rio de Janeiro",
            "Natal", "Porto Alegre", "Porto Velho", "Boa Vista", "Florianópolis",
            "São Paulo", "Aracaju", "Palmas"
        ]

        # Seleciona nomes de cidades aleatórios
        nomes_cidades = random.sample(CAPITAIS_BRASILEIRAS, self._num_cidades)
        
        # Cria as instâncias de Cidade
        for nome in nomes_cidades:
            self._map.append(Cidade(nome))

        # Garante que o mapa seja conectado (grafo conexo)
        # Conecta todas as cidades em um ciclo para garantir a conexão
        for i in range(self._num_cidades):
            cidade_atual = self._map[i]
            proxima_cidade = self._map[(i + 1) % self._num_cidades]
            cidade_atual.adicionar_vizinha(proxima_cidade)

        # Adiciona mais algumas conexões aleatórias para criar mais caminhos
        for cidade_origem in self._map:
            while len(cidade_origem.vizinhas) < self._max_vizinhos_por_cidade:
                cidade_destino = random.choice(self._map)
                if cidade_origem != cidade_destino and cidade_destino not in cidade_origem.vizinhas:
                    cidade_origem.adicionar_vizinha(cidade_destino)

    def getMap(self) -> List[Cidade]:
        return self._map
