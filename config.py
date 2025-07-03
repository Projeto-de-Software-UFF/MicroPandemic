# config.py

# Configurações Gerais do Jogo
MAX_ACTIONS_PER_TURN = 3
MAX_PLAYERS = 4
NUM_CITIES = 5
MAX_NEIGHBORS_PER_CITY = 3 # Um valor razoável para um mapa pequeno

# Distribuição de Cartas no Baralho
# Formato: { "NomeDaCarta": Quantidade }
CARD_DISTRIBUTION = {
    "Teletransporte": 6,
    "ConstruirCentroPesquisa": 6,
    "BloquearInfeccao": 6,
    "TratarDoenca": 6,
    "DescobrirCura": 6,
    "EventoDoenca": 2 # Por cor, então X * 4 cartas de evento
}

# Limites do Jogador
MAX_CARDS_IN_HAND = 7
NUM_INITIAL_CARDS = 5

# Novas Configurações de Regras
DRAW_CARDS_AT_START_OF_TURN = False # True para início, False para fim
SHARED_DECK = False # True para deck compartilhado, False para decks separados
MULTIPLY_DECK_BY_PLAYERS = False # True para multiplicar o deck pelo número de jogadores
DISCOVER_CURE_REQUIRES_RESEARCH_CENTER = True # True se precisar de centro de pesquisa para descobrir a cura
VICTORY_ONLY_BY_ERADICATION = False # Faz com que só seja possível ganhar caso o jogador elimine todos os níveis de todas as doenças

# Frequência de Eventos e Compra de Cartas
INFECTION_PHASE_FREQUENCY = 1 # De quanto em quantos turnos há uma fase de infecção
INFECTIONS_PER_PHASE = 1 # Quantas infecções ocorrem na fase de infecção
NUM_CARDS_TO_DRAW = 2 # Quantas cartas são compradas na fase de compra de cartas

# Configurações de Infecção Inicial
DISTRIBUTE_INITIAL_INFECTION_BY_COLOR = True # Se True, a infecção inicial distribui níveis de doença por cor; se False, adiciona todos os níveis de uma vez.

# Limites de Ações Específicas
MAX_SHARE_CARD_ACTIONS_PER_TURN = 1 # Quantidade máxima de vezes que um jogador pode usar a ação de compartilhar carta por turno

# Configurações de Doença
OUTBREAK_THRESHOLD = 3 # Nível de doença que causa um surto
CRITICAL_DISEASE_LEVEL = 7 # Nível de doença que causa derrota
