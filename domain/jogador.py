from domain.cidade import Cidade
from domain.mao import Mao

class Jogador:   
    def __init__(self, nome: str, posicao: "Cidade"):
        self._nome = nome
        self._posicao = posicao
        self._mao = Mao()

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def posicao(self) -> "Cidade":
        return self._posicao

    @property
    def mao(self) -> "Mao":
        return self._mao

    def mover_para(self, cidade: "Cidade"):
        self._posicao = cidade
        print(f"Jogador {self.nome} movido para {cidade.nome}")
        
    def compartilhar_carta(self, outro_jogador: "Jogador", carta: "Carta") -> bool:
        if self.posicao == outro_jogador.posicao:
            if carta in self.mao.cartas:
                if outro_jogador.mao.adicionar_carta(carta):
                    self.mao.remover_carta(carta)
                    print(f"{self.nome} compartilhou '{carta.nome}' com {outro_jogador.nome}.")
                    return True
                else:
                    print(f"A mão de {outro_jogador.nome} está cheia.")
                    return False
            else:
                print(f"{self.nome} não possui a carta '{carta.nome}'.")
                return False
        else:
            print("Jogadores precisam estar na mesma cidade para compartilhar cartas.")
            return False
        