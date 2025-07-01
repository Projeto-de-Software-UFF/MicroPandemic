from domain.carta.carta import Carta, TipoCarta
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.jogo_controller import Jogo
    from domain.jogador import Jogador

class CompartilharCarta(Carta):
    def __init__(self):
        super().__init__("Compartilhar Carta", TipoCarta.ACAO)

    def ativar(self, jogo: 'Jogo', jogador: 'Jogador', outro_jogador: 'Jogador', carta_a_compartilhar: 'Carta') -> bool:
        print(f"{jogador.nome} usando Compartilhar Carta com {outro_jogador.nome}.")
        return jogador.compartilhar_carta(outro_jogador, carta_a_compartilhar)