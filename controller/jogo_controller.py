from __future__ import annotations
import random
from typing import List, Dict
from domain.baralho import Baralho
from domain.cidade import Cidade
from domain.doenca import Doenca
from domain.jogador import Jogador
from enuns.cor import Cor
from controller.game_map_controller import GameMap
from domain.carta.carta import Carta
import config

class Jogo:
    _instancia = None

    def __init__(self):
        if Jogo._instancia is not None:
            raise Exception("Singleton: Use Jogo.get_instancia()")
        
        self.jogadores: List[Jogador] = []
        self.cidades: Dict[str, Cidade] = {}
        
        self.doencas: Dict[Cor, Doenca] = {}
        self.acoes_restantes: int = config.MAX_ACTIONS_PER_TURN
        self.game_over: bool = False
        self.vitoria: bool = False
        self.jogador_atual_idx: int = 0
        self._infeccao_bloqueada: bool = False
        
        Jogo._instancia = self

    @staticmethod
    def get_instancia() -> "Jogo":
        if Jogo._instancia is None:
            Jogo()
        return Jogo._instancia

    @property
    def jogador_atual(self) -> Jogador:
        return self.jogadores[self.jogador_atual_idx]

    def inicializar_jogo(self, num_jogadores: int = 1):
        # 1. Criar Doenças
        for cor in Cor:
            self.doencas[cor] = Doenca(cor)

        # 2. Criar Cidades e Mapa
        map_controller = GameMap(config.NUM_CITIES, config.MAX_NEIGHBORS_PER_CITY)
        self.cidades = {c.nome: c for c in map_controller.getMap()}
        
        # Inicializa o baralho aqui, pois num_jogadores está disponível
        self.baralho: Baralho = Baralho(num_jogadores)

        # 3. Criar Jogadores
        cidade_inicial = random.choice(list(self.cidades.values()))
        for i in range(num_jogadores):
            self.jogadores.append(Jogador(f"Jogador {i+1}", cidade_inicial))

        # 4. Distribuir Mãos Iniciais
        from domain.carta.carta import TipoCarta # Import here to avoid circular dependency
        for jogador in self.jogadores:
            for _ in range(config.NUM_INITIAL_CARDS): # Usar config.NUM_INITIAL_CARDS
                carta = self.baralho.comprar_carta()
                if carta:
                    if carta.tipo == TipoCarta.EPIDEMIA:
                        print(f"Carta de Evento de Doença comprada na mão inicial: {carta.nome}. Ativando imediatamente.")
                        carta.ativar(self, jogador) # Event cards activate on draw
                    else:
                        jogador.mao.adicionar_carta(carta)

        # 5. Infecção Inicial
        for i in range(3, 0, -1): # 3, 2, 1 níveis de infecção
            cidade_infectada = random.choice(list(self.cidades.values()))
            cor_aleatoria = random.choice(list(Cor))
            cidade_infectada.adicionar_nivel_doenca(cor_aleatoria, i)
            print(f"Infecção inicial: {cidade_infectada.nome} com {i} nível(is) de doença {cor_aleatoria.name}.")

        print("\nJogo iniciado!")

    def mover_jogador(self, jogador: Jogador, cidade_destino: Cidade) -> bool:
        if self.acoes_restantes <= 0:
            print("Sem ações restantes.")
            return False
        
        if cidade_destino in jogador.posicao.vizinhas:
            jogador.mover_para(cidade_destino)
            self.acoes_restantes -= 1
            print(f"Movimento realizado. Ações restantes: {self.acoes_restantes}")
            return True
        else:
            print(f"Movimento inválido: {cidade_destino.nome} não é vizinha de {jogador.posicao.nome}.")
            return False

    def compartilhar_carta_acao(self, jogador_origem: Jogador, jogador_destino: Jogador, carta_a_compartilhar: Carta) -> bool:
        if self.acoes_restantes <= 0:
            print("Sem ações restantes.")
            return False
        
        if len(self.jogadores) < 2:
            print("Não há outros jogadores para compartilhar cartas.")
            return False

        if jogador_origem.compartilhar_carta(jogador_destino, carta_a_compartilhar):
            self.acoes_restantes -= 1
            print(f"Compartilhamento realizado. Ações restantes: {self.acoes_restantes}")
            return True
        return False

    def proximo_turno(self):
        # Gerenciar mão do jogador atual
        jogador = self.jogador_atual
        while len(jogador.mao.cartas) > config.MAX_CARDS_IN_HAND:
            # Na implementação real, o jogador escolheria qual carta descartar
            carta_descartada = jogador.mao.cartas.pop(0) 
            print(f"{jogador.nome} descartou {carta_descartada.nome} por excesso de cartas.")

        # Mudar para o próximo jogador
        self.jogador_atual_idx = (self.jogador_atual_idx + 1) % len(self.jogadores)
        self.acoes_restantes = config.MAX_ACTIONS_PER_TURN
        print(f"\n--- Próximo turno: {self.jogador_atual.nome} ---")

        if config.DRAW_CARDS_AT_START_OF_TURN:
            self.comprar_cartas_fase()

        self.verificar_condicoes_finais()

    def comprar_cartas_fase(self):
        print("\n--- Fase de Compra de Cartas ---")
        for _ in range(config.NUM_CARDS_TO_DRAW): # Compra NUM_CARDS_TO_DRAW cartas
            if self.baralho.esta_vazio():
                print("Derrota! O baralho de jogadores acabou.")
                self.game_over = True
                return

            carta = self.baralho.comprar_carta()
            print(f"{self.jogador_atual.nome} comprou: {carta}")
            
            from domain.carta.carta import TipoCarta # Import here to avoid circular dependency
            if carta.tipo == TipoCarta.EPIDEMIA:
                carta.ativar(self, self.jogador_atual)
            else:
                self.jogador_atual.mao.adicionar_carta(carta)
        
        if not self._infeccao_bloqueada:
            for _ in range(config.INFECTION_FREQUENCY):
                self.fase_infeccao()
        else:
            print("Fase de infecção pulada devido à carta Bloquear Infecção.")
            self._infeccao_bloqueada = False


    def fase_infeccao(self):
        print("\n--- Fase de Infecção ---")
        # Lógica simplificada: infecta uma cidade aleatória
        cidade_a_infectar = random.choice(list(self.cidades.values()))
        cor_infeccao = random.choice(list(Cor))
        print(f"A cidade {cidade_a_infectar.nome} será infectada com a doença {cor_infeccao.name}.")
        cidade_a_infectar.adicionar_nivel_doenca(cor_infeccao, 1)


    def descobrir_cura(self, cor: Cor):
        if not self.doencas[cor].curada:
            self.doencas[cor].curada = True
            print(f"A cura para a doença {cor.name} foi descoberta!")
        self.verificar_condicoes_finais()

    def aplicar_evento_doenca(self, cor: Cor):
        cidade_infectada = random.choice(list(self.cidades.values()))
        cidade_infectada.adicionar_nivel_doenca(cor, 1)
        print(f"EVENTO: {cidade_infectada.nome} teve o nível da doença {cor.name} aumentado.")

    def bloquear_proxima_infeccao(self):
        self._infeccao_bloqueada = True

    def get_doenca(self, cor: Cor) -> Doenca:
        return self.doencas[cor]

    def verificar_condicoes_finais(self):
        # Vitória: todas as 4 doenças curadas
        if all(d.curada for d in self.doencas.values()):
            print("Parabéns! Todas as doenças foram curadas. Vocês venceram!")
            self.vitoria = True
            self.game_over = True

        # Derrota: nível de doença >= 7 em qualquer cidade
        for cidade in self.cidades.values():
            for nivel in cidade.niveis_doenca.values():
                if nivel >= 7:
                    print(f"Derrota! A doença atingiu o nível crítico em {cidade.nome}.")
                    self.game_over = True
                    return
