from __future__ import annotations
from typing import List, Dict
from enuns.cor import Cor
import config

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

    def adicionar_nivel_doenca(self, cor: Cor, quantidade: int, outbreak_cities: set = None):
        if outbreak_cities is None:
            outbreak_cities = set()

        nivel_atual = self._niveis_doenca.get(cor, 0)
        novo_nivel = nivel_atual + quantidade

        self._niveis_doenca[cor] = novo_nivel

        if novo_nivel >= config.OUTBREAK_THRESHOLD and nivel_atual < config.OUTBREAK_THRESHOLD:
            if self not in outbreak_cities:
                outbreak_cities.add(self)
                self.propagar_doenca(cor, outbreak_cities)

    def propagar_doenca(self, cor: Cor, outbreak_cities: set):
        print(f"SURTO em {self.nome} com a doença {cor.name}!")
        for vizinha in self._vizinhas:
            print(f"Propagando para {vizinha.nome}...")
            vizinha.adicionar_nivel_doenca(cor, 1, outbreak_cities)

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