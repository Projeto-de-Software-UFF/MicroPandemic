from domain.carta.carta import Carta, TipoCarta
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.jogo_controller import Jogo
    from domain.jogador import Jogador
    from domain.cidade import Cidade

class Teletransporte(Carta):
    def __init__(self):
        super().__init__("Teletransporte", TipoCarta.EVENTO)

    def ativar(self, jogo: 'Jogo', jogador: 'Jogador', cidade_alvo: 'Cidade') -> bool:
        print(f"{jogador.nome} usando Teletransporte para {cidade_alvo.nome}.")
        jogador.mover_para(cidade_alvo)
        return True