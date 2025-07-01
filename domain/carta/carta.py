from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.jogo_controller import Jogo
    from domain.jogador import Jogador

class TipoCarta(Enum):
    CIDADE = "Cidade"
    EVENTO = "Evento"
    EPIDEMIA = "Epidemia"

class Carta:
    def __init__(self, nome: str, tipo: TipoCarta):
        self._nome = nome
        self._tipo = tipo

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def tipo(self) -> TipoCarta:
        return self._tipo

    def ativar(self, jogo: 'Jogo', jogador: 'Jogador', **kwargs) -> bool:
        # Método a ser sobrescrito pelas subclasses
        print(f"Ativando carta: {self.nome}")
        return True

    def __repr__(self) -> str:
        return f"{self.tipo.value}: {self.nome}