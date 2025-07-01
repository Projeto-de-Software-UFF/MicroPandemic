from __future__ import annotations
from typing import List, Dict
from enuns.cor import Cor

class Cidade:
    def __init__(self, nome: str):
        self._nome = nome
        self._vizinhas: List[Cidade] = []
        self._tem_centro_pesquisa: bool = False
        self._niveis_doenca: Dict[Cor, int] = {cor: 0 for cor in Cor}

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def vizinhas(self) -> List[Cidade]:
        return self._vizinhas

    @property
    def tem_centro_pesquisa(self) -> bool:
        return self._tem_centro_pesquisa
    
    @property
    def niveis_doenca(self) -> Dict[Cor, int]:
        return self._niveis_doenca

    def adicionar_vizinha(self, cidade: Cidade):
        if cidade not in self._vizinhas:
            self._vizinhas.append(cidade)
            cidade.adicionar_vizinha(self) # Conexão bidirecional

    def construir_centro_pesquisa(self):
        if not self._tem_centro_pesquisa:
            self._tem_centro_pesquisa = True

    def adicionar_nivel_doenca(self, cor: Cor, quantidade: int, jogo: 'Jogo', cidades_ja_surtadas: set = None):
        if self in (cidades_ja_surtadas or set()):
            return # Já surtou nesta cadeia de reação

        nivel_atual = self._niveis_doenca.get(cor, 0)
        
        if nivel_atual + quantidade > 3:
            self._niveis_doenca[cor] = 3
            self.propagar_doenca(cor, jogo, cidades_ja_surtadas or {self})
        else:
            self._niveis_doenca[cor] = nivel_atual + quantidade
            # Verifica a condição de derrota aqui
            if self._niveis_doenca[cor] >= 7:
                jogo.game_over = True

    def propagar_doenca(self, cor: Cor, jogo: 'Jogo', cidades_ja_surtadas: set):
        print(f"SURTO em {self.nome} com a doença {cor.name}!")
        cidades_ja_surtadas.add(self)

        for vizinha in self._vizinhas:
            print(f"Propagando para {vizinha.nome}...")
            vizinha.adicionar_nivel_doenca(cor, 1, jogo, cidades_ja_surtadas)

    def reduzir_nivel_doenca(self, cor: Cor, quantidade: int):
        self._niveis_doenca[cor] = max(0, self._niveis_doenca.get(cor, 0) - quantidade)

    def remover_toda_doenca_de_cor(self, cor: Cor):
        self._niveis_doenca[cor] = 0

    def get_nivel_doenca(self, cor: Cor) -> int:
        return self._niveis_doenca.get(cor, 0)

    def __repr__(self) -> str:
        doencas_str = ", ".join([f"{cor.name[0]}:{nivel}" for cor, nivel in self._niveis_doenca.items() if nivel > 0])
        centro_str = " [CP]" if self._tem_centro_pesquisa else ""
        return f"{self.nome}{centro_str} ({doencas_str})"