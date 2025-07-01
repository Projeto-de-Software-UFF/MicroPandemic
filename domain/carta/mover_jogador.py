from domain.carta.carta import Carta, TipoCarta
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.jogo_controller import Jogo
    from domain.jogador import Jogador
    from domain.cidade import Cidade

class MoverJogador(Carta):
    def __init__(self):
        super().__init__("Mover Jogador", TipoCarta.EVENTO)

    def ativar(self, jogo: 'Jogo', jogador: 'Jogador', cidade_alvo: 'Cidade') -> bool:
        print(f"{jogador.nome} usando Mover Jogador para {cidade_alvo.nome}.")
        jogo.mover_jogador(jogador, cidade_alvo)
        return True