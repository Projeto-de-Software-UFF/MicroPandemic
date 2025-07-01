from terminal_view.header import header
from terminal_view.menu import menu
from terminal_view.painel import painel
from terminal_view.view_map import viewMap
from controller.jogo_controller import Jogo

def exibir_estado_jogo(jogo: Jogo):
    """Função auxiliar para exibir o estado atual do jogo."""
    header(jogo.jogador_atual_idx + 1) # Turno pode ser associado ao jogador
    painel(
        acoes_restantes=jogo.acoes_restantes,
        jogador_atual=jogo.jogador_atual,
        curas_descobertas=[cor.name for cor, doenca in jogo.doencas.items() if doenca.curada]
    )
    viewMap(list(jogo.cidades.values()))
    print("\nSua mão:")
    print(jogo.jogador_atual.mao)

def main():
    # --- Configuração Inicial ---
    jogo = Jogo.get_instancia()
    try:
        num_jogadores = int(input("Digite o número de jogadores (1-4): "))
        if not 1 <= num_jogadores <= 4:
            raise ValueError
    except ValueError:
        print("Número inválido. Iniciando com 1 jogador.")
        num_jogadores = 1
    
    jogo.inicializar_jogo(num_jogadores)

    # --- Loop Principal do Jogo ---
    while not jogo.game_over:
        exibir_estado_jogo(jogo)
        
        jogador = jogo.jogador_atual

        if jogo.acoes_restantes > 0:
            menu()
            opcao = input("Digite sua ação: ").lower()

            if opcao == '0':
                print("Saindo do jogo...")
                break
            
            elif opcao == '1': # Mover-se
                vizinhas = jogador.posicao.vizinhas
                if not vizinhas:
                    print("Não há cidades vizinhas para onde se mover.")
                else:
                    print("\nEscolha uma cidade vizinha para se mover:")
                    for i, cidade in enumerate(vizinhas):
                        print(f"{i+1}. {cidade.nome}")
                    try:
                        cidade_idx = int(input("Digite o número da cidade: ")) - 1
                        if 0 <= cidade_idx < len(vizinhas):
                            jogo.mover_jogador(jogador, vizinhas[cidade_idx])
                        else:
                            print("Seleção inválida.")
                    except ValueError:
                        print("Entrada inválida.")

            elif opcao == '2': # Tratar doença
                doencas_na_cidade = {cor: nivel for cor, nivel in jogador.posicao.niveis_doenca.items() if nivel > 0}
                if not doencas_na_cidade:
                    print(f"Não há doenças em {jogador.posicao.nome}.")
                else:
                    print("\nEscolha uma doença para tratar:")
                    cores = list(doencas_na_cidade.keys())
                    for i, cor in enumerate(cores):
                        print(f"{i+1}. {cor.name}")
                    try:
                        cor_idx = int(input("Digite o número da doença: ")) - 1
                        if 0 <= cor_idx < len(cores):
                            jogo.tratar_doenca(jogador, cores[cor_idx])
                        else:
                            print("Seleção inválida.")
                    except ValueError:
                        print("Entrada inválida.")

            elif opcao == '3': # Usar carta
                if not jogador.mao.cartas:
                    print("Sua mão está vazia.")
                else:
                    print("\nEscolha uma carta para usar:")
                    print(jogador.mao)
                    try:
                        carta_idx = int(input("Digite o número da carta: ")) - 1
                        carta_selecionada = jogador.mao.cartas[carta_idx]
                        
                        kwargs = {}
                        # Coleta de input específico para cada carta que precisa
                        if "Teletransporte" in carta_selecionada.nome:
                            print("\nEscolha a cidade de destino:")
                            cidades = list(jogo.cidades.values())
                            for i, c in enumerate(cidades):
                                print(f"{i+1}. {c.nome}")
                            cidade_idx = int(input("Digite o número da cidade: ")) - 1
                            kwargs['cidade_alvo'] = cidades[cidade_idx]
                        
                        jogo.usar_carta(jogador, carta_selecionada, **kwargs)

                    except (ValueError, IndexError):
                        print("Seleção inválida.")

            elif opcao == '4': # Passar turno
                print("Você escolheu finalizar seu turno.")
                jogo.acoes_restantes = 0

            else:
                print("Opção inválida.")

        # Se acabaram as ações, finaliza o turno
        if jogo.acoes_restantes <= 0:
            jogo.finalizar_turno()
            if not jogo.game_over:
                input("\nPressione Enter para iniciar o próximo turno...")


    # --- Fim de Jogo ---
    if jogo.vitoria:
        print("\nFIM DE JOGO: VITÓRIA!")
    else:
        print("\nFIM DE JOGO: DERROTA!")

if __name__ == "__main__":
    main()
