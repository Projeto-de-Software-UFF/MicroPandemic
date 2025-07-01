from __future__ import annotations
import random
from typing import List
from domain.cidade import Cidade

class BaralhoInfeccao:
    def __init__(self, cidades: List[Cidade]):
        self._cartas: List[Cidade] = list(cidades)
        self._descarte: List[Cidade] = []
        self.embaralhar()

    def embaralhar(self):
        random.shuffle(self._cartas)

    def comprar_carta(self) -> Cidade | None:
        if not self._cartas:
            self.reembaralhar_descarte()
            if not self._cartas:
                return None # Não deveria acontecer em um jogo normal
        
        cidade_infectada = self._cartas.pop(0)
        self._descarte.append(cidade_infectada)
        return cidade_infectada

    def reembaralhar_descarte(self):
        print("\nAVISO: O baralho de infecção será reembaralhado!")
        random.shuffle(self._descarte)
        self._cartas.extend(self._descarte)
        self._descarte.clear()

