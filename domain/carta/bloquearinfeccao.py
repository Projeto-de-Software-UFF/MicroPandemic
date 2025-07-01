from domain.carta.carta import Carta, TipoCarta
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.jogo_controller import Jogo
    from domain.jogador import Jogador

class BloquearInfeccao(Carta):
    def __init__(self):
        super().__init__("Bloquear Infecção", TipoCarta.ACAO)

    def ativar(self, jogo: 'Jogo', jogador: 'Jogador', **kwargs) -> bool:
        print(f"{jogador.nome} ativou Bloquear Infecção.")
        jogo.bloquear_proxima_infeccao()
        return True