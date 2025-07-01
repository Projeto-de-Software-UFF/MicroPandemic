from typing import List
from domain.cidade import Cidade

def viewMap(cidades: List[Cidade]):
    """
    Exibe o mapa do jogo, mostrando as cidades, suas conexões e estado atual.
    """
    print("\n" + "="*15 + " MAPA DO MUNDO " + "="*15)
    
    for cidade in cidades:
        # Detalhes da cidade
        print(f"\n--- {cidade.nome.upper()} ---")
        
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