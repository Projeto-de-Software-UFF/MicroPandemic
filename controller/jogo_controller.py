from __future__ import annotations
import random
from typing import List, Dict
from domain.baralho import Baralho
from domain.cidade import Cidade
from domain.doenca import Doenca
from domain.jogador import Jogador
from enuns.cor import Cor
from domain.baralho_infeccao import BaralhoInfeccao

class Jogo:
    _instancia = None

    def __init__(self):
        if Jogo._instancia is not None:
            raise Exception("Singleton: Use Jogo.get_instancia()")
        
        self.jogadores: List[Jogador] = []
        self.cidades: Dict[str, Cidade] = {}
        self.baralho: Baralho = Baralho()
        self.doencas: Dict[Cor, Doenca] = {}
        self.baralho_infeccao: BaralhoInfeccao = None
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

        # 2. Criar Cidades, Mapa e Baralho de Infecção
        map_controller = GameMap()
        self.cidades = {c.nome: c for c in map_controller.getMap()}
        self.baralho_infeccao = BaralhoInfeccao(list(self.cidades.values()))
        
        # 3. Criar Jogadores
        cidade_inicial = random.choice(list(self.cidades.values()))
        for i in range(num_jogadores):
            self.jogadores.append(Jogador(f"Jogador {i+1}", cidade_inicial))

        # 4. Distribuir Mãos Iniciais
        for jogador in self.jogadores:
            for _ in range(5): # 5 cartas iniciais
                carta = self.baralho.comprar_carta()
                if carta:
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

    def finalizar_turno(self):
        if self.game_over:
            return

        print(f"\n--- Finalizando o turno de {self.jogador_atual.nome} ---")
        
        # 2. Comprar cartas
        self._fase_compra_cartas()
        if self.game_over: return

        # 3. Gerenciar mão
        self._gerenciar_mao()

        # 4. Fase de Infecção (se não bloqueada)
        if not self._infeccao_bloqueada:
            self._fase_infeccao()
            if self.game_over: return
        else:
            print("Fase de infecção pulada devido à carta Bloquear Infecção.")
            self._infeccao_bloqueada = False

        # 5. Passar para o próximo jogador
        self.jogador_atual_idx = (self.jogador_atual_idx + 1) % len(self.jogadores)
        self.acoes_restantes = 5 # Reset das ações para o próximo
        print(f"\n--- Próximo turno: {self.jogador_atual.nome} ---")
        self.verificar_condicoes_finais()

    def _gerenciar_mao(self):
        jogador = self.jogador_atual
        while len(jogador.mao.cartas) > 7:
            # Na implementação real, o jogador escolheria qual carta descartar
            # Aqui, vamos descartar a primeira carta da mão
            carta_descartada = jogador.mao.cartas.pop(0) 
            self.baralho.descartar_carta(carta_descartada)
            print(f"{jogador.nome} descartou {carta_descartada.nome} por excesso de cartas.")

    def _fase_compra_cartas(self):
        print("\n--- Fase de Compra de Cartas ---")
        for _ in range(1): # Compra 1 carta
            if self.baralho.esta_vazio():
                print("Derrota! O baralho de jogadores acabou.")
                self.game_over = True
                return

            carta = self.baralho.comprar_carta()
            print(f"{self.jogador_atual.nome} comprou: {carta}")
            
            if carta.tipo.name == 'EVENTO_DOENCA':
                carta.ativar(self, self.jogador_atual)
            else:
                self.jogador_atual.mao.adicionar_carta(carta)

    def _fase_infeccao(self):
        print("\n--- Fase de Infecção ---")
        taxa_infeccao = 2 # Exemplo: 2 cidades por turno

        for _ in range(taxa_infeccao):
            cidade_a_infectar = self.baralho_infeccao.comprar_carta()
            if cidade_a_infectar:
                cor_infeccao = random.choice(list(Cor)) # A cor ainda é aleatória
                print(f"A cidade {cidade_a_infectar.nome} será infectada com a doença {cor_infeccao.name}.")
                cidade_a_infectar.adicionar_nivel_doenca(cor_infeccao, 1, self)
                self.verificar_condicoes_finais()
                if self.game_over:
                    break


    def descobrir_cura(self, cor: Cor):
        if not self.doencas[cor].curada:
            self.doencas[cor].curada = True
            print(f"A cura para a doença {cor.name} foi descoberta!")
        self.verificar_condicoes_finais()

    def tratar_doenca(self, jogador: Jogador, cor: Cor) -> bool:
        if self.acoes_restantes <= 0:
            print("Sem ações restantes.")
            return False

        cidade_atual = jogador.posicao
        if cidade_atual.get_nivel_doenca(cor) <= 0:
            print(f"Não há doença {cor.name} para tratar em {cidade_atual.nome}.")
            return False

        doenca = self.get_doenca(cor)
        if doenca.curada:
            cidade_atual.remover_toda_doenca_de_cor(cor)
            print(f"A doença {cor.name} foi erradicada de {cidade_atual.nome}!")
        else:
            cidade_atual.reduzir_nivel_doenca(cor, 1)
            print(f"Um nível da doença {cor.name} foi tratado em {cidade_atual.nome}.")
        
        self.acoes_restantes -= 1
        return True

    def usar_carta(self, jogador: Jogador, carta: "Carta", **kwargs) -> bool:
        if self.acoes_restantes <= 0:
            print("Sem ações restantes.")
            return False
        
        sucesso = carta.ativar(self, jogador, **kwargs)
        if sucesso:
            jogador.mao.remover_carta(carta)
            self.baralho.descartar_carta(carta)
            self.acoes_restantes -= 1
        return sucesso

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