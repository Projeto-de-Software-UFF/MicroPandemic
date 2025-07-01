from domain.carta.carta import Carta, TipoCarta
from enuns.cor import Cor
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from controller.jogo_controller import Jogo
    from domain.jogador import Jogador

class DescobrirCura(Carta):
    def __init__(self, cor: Cor):
        super().__init__(f"Descobrir Cura {cor.name.capitalize()}", TipoCarta.ACAO)
        self._cor = cor

    @property
    def cor(self) -> Cor:
        return self._cor

    def ativar(self, jogo: 'Jogo', jogador: 'Jogador', **kwargs) -> bool:
        if jogador.posicao.tem_centro_pesquisa:
            print(f"{jogador.nome} está tentando descobrir a cura para a doença {self.cor.name}.")
            # Lógica para verificar se o jogador tem as cartas necessárias para descobrir a cura
            # Por simplicidade, aqui apenas marca como curada se estiver em centro de pesquisa
            jogo.descobrir_cura(self.cor)
            return True
        else:
            print("Você precisa estar em um Centro de Pesquisa para descobrir a cura.")
            return False