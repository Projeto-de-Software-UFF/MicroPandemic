from domain.carta.carta import Carta, TipoCarta
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.jogo_controller import Jogo
    from domain.jogador import Jogador

class ConstruirCentroPesquisa(Carta):
    def __init__(self):
        super().__init__("Construir Centro de Pesquisa", TipoCarta.EVENTO)

    def ativar(self, jogo: 'Jogo', jogador: 'Jogador', **kwargs) -> bool:
        print(f"{jogador.nome} está construindo um Centro de Pesquisa em {jogador.posicao.nome}.")
        jogador.posicao.construir_centro_pesquisa()
        return True