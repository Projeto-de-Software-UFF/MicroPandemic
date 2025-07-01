from terminal_view.header import header
from terminal_view.menu import menu
from terminal_view.painel import painel
from terminal_view.view_map import viewMap
from controller.jogo_controller import Jogo
import config

def exibir_estado_jogo(jogo: Jogo):
    """Função auxiliar para exibir o estado atual do jogo."""
    header(jogo.jogador_atual_idx + 1) # Turno pode ser associado ao jogador
    painel(
        acoes_restantes=jogo.acoes_restantes,
        jogador_atual=jogo.jogador_atual,
        curas_descobertas=[cor.name for cor, doenca in jogo.doencas.items() if doenca.curada]
    )
    viewMap(list(jogo.cidades.values()), jogo.jogadores)
    print("\nSua mão:")
    print(jogo.jogador_atual.mao)

def main():
    # --- Configuração Inicial ---
    jogo = Jogo.get_instancia()
    try:
        num_jogadores = int(input(f"Digite o número de jogadores (1-{config.MAX_PLAYERS}): "))
        if not 1 <= num_jogadores <= config.MAX_PLAYERS:
            raise ValueError
    except ValueError:
        print("Número inválido. Iniciando com 1 jogador.")
        num_jogadores = 1
    
    jogo.inicializar_jogo(num_jogadores)

    # --- Loop Principal do Jogo ---
    while not jogo.game_over:
        exibir_estado_jogo(jogo)
        
        jogador = jogo.jogador_atual

        # Logic for drawing cards based on config
        if config.DRAW_CARDS_AT_START_OF_TURN:
            # If cards are drawn at the start of the turn, the drawing phase already occurred in proximo_turno
            pass
        else:
            # If cards are drawn at the end of the turn, check if actions are over to start the drawing phase
            if jogo.acoes_restantes <= 0:
                jogo.comprar_cartas_fase()
                if not jogo.game_over:
                    jogo.proximo_turno()
                input("Pressione Enter para iniciar o próximo turno...")
                continue # Skip the rest of the loop for the next turn

        if jogo.acoes_restantes > 0:
            menu()
            opcao = input("Digite sua ação: ").lower()

            if opcao == '0':
                print("Saindo do jogo...")
                break
            
            elif opcao == '1': # Usar carta
                if not jogador.mao.cartas:
                    print("Sua mão está vazia. Nenhuma carta para usar.")
                    input("Pressione Enter para continuar...")
                    continue

                try:
                    print("\nEscolha uma carta para usar:")
                    print(jogador.mao)
                    carta_idx = int(input("Digite o número da carta: ")) - 1
                    
                    carta_selecionada = jogador.mao.cartas[carta_idx]
                    kwargs = {}

                    # Lógica específica para cartas que precisam de input do usuário
                    if carta_selecionada.nome == "Teletransporte":
                        print("\nEscolha a cidade de destino:")
                        for i, cidade in enumerate(jogo.cidades.values()):
                            print(f"{i+1}. {cidade.nome}")
                        cidade_idx = int(input("Digite o número da cidade: ")) - 1
                        kwargs["cidade_alvo"] = list(jogo.cidades.values())[cidade_idx]

                    elif carta_selecionada.nome.startswith("Tratar Doença") or carta_selecionada.nome.startswith("Descobrir Cura"):
                        kwargs["cor"] = carta_selecionada.cor

                    # Ação de Ativar a Carta
                    sucesso = carta_selecionada.ativar(jogo, jogador, **kwargs)

                    if sucesso:
                        jogador.mao.remover_carta(carta_selecionada)
                        jogo.acoes_restantes -= 1
                        print(f"Ação realizada. Ações restantes: {jogo.acoes_restantes}")
                    else:
                        print("A ação não pôde ser concluída.")

                except (ValueError, IndexError):
                    print("Seleção inválida.")
                
                input("Pressione Enter para continuar...")

            elif opcao == '2': # Mover-se
                vizinhas = jogador.posicao.vizinhas
                if not vizinhas:
                    print("Não há cidades vizinhas para onde se mover.")
                    input("Pressione Enter para continuar...")
                    continue
                
                print("\nEscolha uma cidade vizinha para se mover:")
                for i, cidade in enumerate(vizinhas):
                    print(f"{i+1}. {cidade.nome}")
                
                try:
                    cidade_idx = int(input("Digite o número da cidade: ")) - 1
                    if 0 <= cidade_idx < len(vizinhas):
                        cidade_escolhida = vizinhas[cidade_idx]
                        jogo.mover_jogador(jogador, cidade_escolhida)
                    else:
                        print("Seleção inválida.")
                except ValueError:
                    print("Entrada inválida.")
                
                input("Pressione Enter para continuar...")

            elif opcao == '3': # Compartilhar Carta
                if len(jogo.jogadores) <= 1:
                    print("Não é possível compartilhar cartas com apenas um jogador.")
                    input("Pressione Enter para continuar...")
                    continue
                
                if not jogador.mao.cartas:
                    print("Sua mão está vazia. Nenhuma carta para compartilhar.")
                    input("Pressione Enter para continuar...")
                    continue

                try:
                    print("\nEscolha o jogador para compartilhar a carta:")
                    jogadores_disponiveis = [p for p in jogo.jogadores if p != jogador]
                    for i, p in enumerate(jogadores_disponiveis):
                        print(f"{i+1}. {p.nome}")
                    
                    jogador_idx = int(input("Digite o número do jogador: ")) - 1
                    outro_jogador = jogadores_disponiveis[jogador_idx]

                    print("\nEscolha a carta para compartilhar:")
                    print(jogador.mao)
                    carta_compartilhar_idx = int(input("Digite o número da carta: ")) - 1
                    carta_a_compartilhar = jogador.mao.cartas[carta_compartilhar_idx]

                    sucesso = jogo.compartilhar_carta_acao(jogador, outro_jogador, carta_a_compartilhar)

                    if sucesso:
                        print("Carta compartilhada com sucesso!")
                    else:
                        print("Não foi possível compartilhar a carta.")

                except (ValueError, IndexError):
                    print("Seleção inválida.")
                
                input("Pressione Enter para continuar...")

            elif opcao == '4': # Passar turno
                print("Você escolheu passar as ações restantes.")
                jogo.acoes_restantes = 0

            else:
                print("Opção inválida.")
                input("Pressione Enter para continuar...")

        # Se acabaram as ações, avança para a próxima fase
        if jogo.acoes_restantes <= 0:
            if not jogo.game_over:
                jogo.proximo_turno()
            input("Pressione Enter para iniciar o próximo turno...")


    # --- Fim de Jogo ---
    if jogo.vitoria:
        print("\nFIM DE JOGO: VITÓRIA!")
    else:
        print("\nFIM DE JOGO: DERROTA!")

if __name__ == "__main__":
    main()
