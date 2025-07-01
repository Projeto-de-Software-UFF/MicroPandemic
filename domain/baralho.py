import random
from typing import List
from domain.carta.carta import Carta
from domain.carta.tratar_doenca import TratarDoenca
from domain.carta.descobrir_cura import DescobrirCura
from domain.carta.teletransporte import Teletransporte

from domain.carta.bloquearinfeccao import BloquearInfeccao
from domain.carta.construircentropesquisa import ConstruirCentroPesquisa
from domain.carta.eventodoenca import EventoDoenca
from enuns.cor import Cor
import config

class Baralho:
    def __init__(self, num_jogadores: int = 1):
        self._cartas: List[Carta] = []
        self._descarte: List[Carta] = []
        self._inicializar_baralho(num_jogadores)
        self.embaralhar()

    def _inicializar_baralho(self, num_jogadores: int):
        multiplicador = num_jogadores if config.MULTIPLY_DECK_BY_PLAYERS else 1

        # Cartas de Ação
        for card_name, quantity in config.CARD_DISTRIBUTION.items():
            for _ in range(quantity * multiplicador):
                if card_name == "Teletransporte":
                    self._cartas.append(Teletransporte())
                elif card_name == "ConstruirCentroPesquisa":
                    self._cartas.append(ConstruirCentroPesquisa())
                elif card_name == "BloquearInfeccao":
                    self._cartas.append(BloquearInfeccao())
                elif card_name == "TratarDoenca":
                    self._cartas.append(TratarDoenca(random.choice(list(Cor))))
                elif card_name == "DescobrirCura":
                    self._cartas.append(DescobrirCura(random.choice(list(Cor))))
                elif card_name == "EventoDoenca":
                    for cor in Cor:
                        self._cartas.append(EventoDoenca(cor))

    def embaralhar(self):
        random.shuffle(self._cartas)

    def comprar_carta(self) -> Carta | None:
        if self.esta_vazio():
            return None
        carta = self._cartas.pop()
        self._descarte.append(carta)
        return carta

    def esta_vazio(self) -> bool:
        return len(self._cartas) == 0

    def __len__(self):
        return len(self._cartas)
