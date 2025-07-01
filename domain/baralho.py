import random
from typing import List
from domain.carta.carta import Carta
from domain.carta.tratar_doenca import TratarDoenca
from domain.carta.descobrir_cura import DescobrirCura
from domain.carta.teletransporte import Teletransporte
from domain.carta.mover_jogador import MoverJogador
from domain.carta.compartilhar_carta import CompartilharCarta
from domain.carta.bloquearinfeccao import BloquearInfeccao
from domain.carta.construircentropesquisa import ConstruirCentroPesquisa
from domain.carta.eventodoenca import EventoDoenca
from enuns.cor import Cor

class Baralho:
    def __init__(self):
        self._cartas: List[Carta] = []
        self._descarte: List[Carta] = []
        self._inicializar_baralho()
        self.embaralhar()

    def _inicializar_baralho(self):
        # Cartas de Ação (5 de cada, conforme escopo)
        for _ in range(5):
            self._cartas.append(Teletransporte())
            self._cartas.append(MoverJogador())
            self._cartas.append(ConstruirCentroPesquisa())
            self._cartas.append(CompartilharCarta())
            self._cartas.append(BloquearInfeccao())
            for cor in Cor:
                self._cartas.append(TratarDoenca(cor))
                self._cartas.append(DescobrirCura(cor))

        # Cartas de Evento de Doença (2 de cada cor, conforme escopo)
        for _ in range(2):
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
