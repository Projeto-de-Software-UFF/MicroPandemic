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
        # 7 tipos de carta * 5 cópias = 35 cartas
        for _ in range(5):
            self._cartas.append(Teletransporte())
            self._cartas.append(MoverJogador())
            self._cartas.append(ConstruirCentroPesquisa())
            self._cartas.append(CompartilharCarta())
            self._cartas.append(BloquearInfeccao())
            # TratarDoenca e DescobrirCura são específicas por cor, mas contam como tipos
            # O escopo pode ser interpretado de formas diferentes.
            # Vamos assumir que são 5 cartas de Tratar e 5 de Descobrir no total.
            # Para simplificar, vamos criar uma de cada cor e uma extra de uma cor aleatória.
            # A melhor abordagem seria ter cartas de cidade, que não estão no escopo.
            # Por ora, vamos seguir uma lógica mais simples e próxima do escopo.
            # Ações que não dependem de cor:
            self._cartas.append(Teletransporte())
            self._cartas.append(MoverJogador())
            self._cartas.append(ConstruirCentroPesquisa())
            self._cartas.append(CompartilharCarta())
            self._cartas.append(BloquearInfeccao())

        # Ações que dependem de cor (vamos criar 5 de cada no total)
        for cor in Cor:
            # Adiciona 1 de cada cor garantido
            self._cartas.append(TratarDoenca(cor))
            self._cartas.append(DescobrirCura(cor))
        
        # Adiciona mais uma carta de Tratar e Descobrir de cor aleatória para totalizar 5
        self._cartas.append(TratarDoenca(random.choice(list(Cor))))
        self._cartas.append(DescobrirCura(random.choice(list(Cor))))


        # Cartas de Evento de Doença (2 de cada cor, conforme escopo)
        for _ in range(2):
            for cor in Cor:
                self._cartas.append(EventoDoenca(cor))

    def descartar_carta(self, carta: Carta):
        self._descarte.append(carta)

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
