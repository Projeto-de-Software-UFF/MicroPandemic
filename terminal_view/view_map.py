from typing import List
from domain.cidade import Cidade
from domain.jogador import Jogador

def viewMap(cidades: List[Cidade], jogadores: List[Jogador]):
    """
    Exibe o mapa do jogo, mostrando as cidades, suas conexões, estado atual e a posição dos jogadores.
    """
    print("\n" + "="*15 + " MAPA DO MUNDO " + "="*15)
    
    for cidade in cidades:
        # Detalhes da cidade
        print(f"\n--- {cidade.nome.upper()} ---")
        
        # Jogadores na cidade
        jogadores_na_cidade = [j.nome for j in jogadores if j.posicao == cidade]
        if jogadores_na_cidade:
            print(f"  [P] Jogadores: {', '.join(jogadores_na_cidade)}")

        # Centro de Pesquisa
        if cidade.tem_centro_pesquisa:
            print("  [+] Possui Centro de Pesquisa")
            
        # Níveis de Doença
        print("  Níveis de Doença:")
        doencas_presentes = False
        for cor, nivel in cidade.niveis_doenca.items():
            if nivel > 0:
                print(f"    - {cor.name.capitalize()}: {nivel}")
                doencas_presentes = True
        if not doencas_presentes:
            print("    Nenhuma")
            
        # Cidades Vizinhas
        print("  Cidades Vizinhas:")
        if cidade.vizinhas:
            print(f"    -> {', '.join([v.nome for v in cidade.vizinhas])}")
        else:
            print("    Nenhuma")
            
    print("\n" + "="*48)