from domain.carta.carta import Carta, TipoCarta
from enuns.cor import Cor
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.jogo_controller import Jogo
    from domain.jogador import Jogador

class EventoDoenca(Carta):
    def __init__(self, cor: Cor):
        super().__init__(f"Evento de Doença {cor.name.capitalize()}", TipoCarta.EPIDEMIA)
        self._cor = cor

    @property
    def cor(self) -> Cor:
        return self._cor

    def ativar(self, jogo: 'Jogo', jogador: 'Jogador', **kwargs) -> bool:
        print(f"Um evento de doença {self.cor.name} ocorreu!")
        jogo.aplicar_evento_doenca(self.cor)
        return True