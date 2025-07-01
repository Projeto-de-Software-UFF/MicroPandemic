import random
from typing import List
from domain.cidade import Cidade

NUM_CIDADES = 5
CAPITAIS_BRASILEIRAS = [
    "Rio Branco", "Maceió", "Macapá", "Manaus", "Salvador", "Fortaleza", "Brasília",
    "Vitória", "Goiânia", "São Luís", "Cuiabá", "Campo Grande", "Belo Horizonte",
    "Belém", "João Pessoa", "Curitiba", "Recife", "Teresina", "Rio de Janeiro",
    "Natal", "Porto Alegre", "Porto Velho", "Boa Vista", "Florianópolis",
    "São Paulo", "Aracaju", "Palmas"
]

class GameMap:
    def __init__(self):
        self._map: List[Cidade] = []
        self._criar_mapa()

    def _criar_mapa(self):
        # Seleciona nomes de cidades aleatórios
        nomes_cidades = random.sample(CAPITAIS_BRASILEIRAS, NUM_CIDADES)
        
        # Cria as instâncias de Cidade
        for nome in nomes_cidades:
            self._map.append(Cidade(nome))

        # Garante que o mapa seja conectado (grafo conexo)
        # Conecta todas as cidades em um ciclo para garantir a conexão
        for i in range(NUM_CIDADES):
            cidade_atual = self._map[i]
            proxima_cidade = self._map[(i + 1) % NUM_CIDADES]
            cidade_atual.adicionar_vizinha(proxima_cidade)

        # Adiciona mais algumas conexões aleatórias para criar mais caminhos
        num_conexoes_adicionais = NUM_CIDADES // 2
        for _ in range(num_conexoes_adicionais):
            cidade1, cidade2 = random.sample(self._map, 2)
            # Evita adicionar uma conexão que já existe
            if cidade2 not in cidade1.vizinhas:
                cidade1.adicionar_vizinha(cidade2)

    def getMap(self) -> List[Cidade]:
        return self._map
