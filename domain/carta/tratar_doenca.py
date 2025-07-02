from domain.carta.carta import Carta, TipoCarta
from enuns.cor import Cor
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.jogo_controller import Jogo
    from domain.jogador import Jogador

class TratarDoenca(Carta):
    def __init__(self, cor: Cor):
        super().__init__(f"Tratar Doença {cor.name.capitalize()}", TipoCarta.ACAO)
        self._cor = cor

    @property
    def cor(self) -> Cor:
        return self._cor

    def ativar(self, jogo: 'Jogo', jogador: 'Jogador', **kwargs) -> bool:
        print(f"{jogador.nome} está tratando a doença {self.cor.name} em {jogador.posicao.nome}.")
        if jogo.get_doenca(self.cor).curada and jogador.posicao.tem_centro_pesquisa:
            jogador.posicao.remover_toda_doenca_de_cor(self.cor)
            print(f"Doença {self.cor.name} completamente erradicada de {jogador.posicao.nome} devido à cura e centro de pesquisa!")
        else:
            jogador.posicao.reduzir_nivel_doenca(self.cor, 1)
        return True