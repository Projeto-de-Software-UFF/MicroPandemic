from enum import Enum

class Baralho(str, Enum):
    DESCOBRIR_CURA = "Descobrir Cura"
    BLOQUEAR_INFECCAO = "Bloquear Infeccao"
    RETARDAR_DOENCA = "Retardar Doenca"
    EVENTO_DOENCA = "Evento Doenca"
    TELETRANSPORTE = "Teletransporte"
    MOVER_JOGADOR = "Mover Jogador"
    CONSTRUIR_CENTRO_PESQUISA = "Construir Centro Pesquisa"
