from typing import List
from domain.jogador import Jogador

def painel(acoes_restantes: int, jogador_atual: Jogador, curas_descobertas: List[str], cartas_restantes_deck: int):
    """
    Exibe o painel de informações do turno atual.
    """
    print("-" * 40)
    print(f"| Jogador Atual: {jogador_atual.nome}".ljust(39) + "|")
    print(f"| Localização: {jogador_atual.posicao.nome}".ljust(39) + "|")
    print(f"| Ações Restantes: {acoes_restantes}".ljust(39) + "|")
    print(f"| Cartas na Mão: {len(jogador_atual.mao)}".ljust(39) + "|")
    print(f"| Cartas Restantes no Deck: {cartas_restantes_deck}".ljust(39) + "|")
    print(f"| Curas Descobertas: {', '.join(curas_descobertas) if curas_descobertas else 'Nenhuma'}".ljust(39) + "|")
    print("-" * 40)