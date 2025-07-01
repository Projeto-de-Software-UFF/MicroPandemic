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

# Novas Configurações de Regras
DRAW_CARDS_AT_START_OF_TURN = False # True para início, False para fim
SHARED_DECK = True # True para deck compartilhado, False para decks separados
MULTIPLY_DECK_BY_PLAYERS = False # True para multiplicar o deck pelo número de jogadores
DISCOVER_CURE_REQUIRES_RESEARCH_CENTER = True # True se precisar de centro de pesquisa para descobrir a cura

# Frequência de Eventos e Compra de Cartas
INFECTION_PHASE_FREQUENCY = 1 # De quanto em quantos turnos há uma fase de infecção
INFECTIONS_PER_PHASE = 1 # Quantas infecções ocorrem na fase de infecção
