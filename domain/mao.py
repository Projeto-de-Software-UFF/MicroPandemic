from typing import List
from domain.carta.carta import Carta
import config

class Mao:
    def __init__(self):
        self._cartas: List[Carta] = []
        self._limite_cartas = config.MAX_CARDS_IN_HAND

    @property
    def cartas(self) -> List[Carta]:
        return self._cartas

    def adicionar_carta(self, carta: Carta) -> bool:
        if not self.esta_cheia():
            self._cartas.append(carta)
            return True
        return False

    def remover_carta(self, carta: Carta) -> bool:
        if carta in self._cartas:
            self._cartas.remove(carta)
            return True
        return False

    def esta_cheia(self) -> bool:
        return len(self._cartas) >= self._limite_cartas

    def __len__(self):
        return len(self._cartas)

    def __str__(self):
        if not self._cartas:
            return "A mão está vazia."
        return "\n".join([f"{i+1}. {carta}" for i, carta in enumerate(self._cartas)])

