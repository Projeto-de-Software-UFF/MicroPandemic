# config.py

# Configurações Gerais do Jogo
MAX_ACTIONS_PER_TURN = 3
MAX_PLAYERS = 4
NUM_CITIES = 5
MAX_NEIGHBORS_PER_CITY = 3 # Um valor razoável para um mapa pequeno

# Distribuição de Cartas no Baralho
# Formato: { "NomeDaCarta": Quantidade }
CARD_DISTRIBUTION = {
    "Teletransporte": 5,
    "ConstruirCentroPesquisa": 5,
    "BloquearInfeccao": 5,
    "TratarDoenca": 5,
    "DescobrirCura": 5,
    "EventoDoenca": 2 # Por cor, então 2 * 4 cores = 8 cartas de evento
}

# Limites do Jogador
MAX_CARDS_IN_HAND = 7
NUM_INITIAL_CARDS = 5
