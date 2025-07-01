from enuns.cor import Cor

class Doenca:
    def __init__(self, cor: Cor):
        self._cor = cor
        self._curada = False

    @property
    def cor(self) -> Cor:
        return self._cor

    @property
    def curada(self) -> bool:
        return self._curada

    @curada.setter
    def curada(self, status: bool):
        self._curada = status

    def __repr__(self):
        status = "Curada" if self._curada else "Ativa"
        return f"Doença {self._cor.name.capitalize()} ({status})"