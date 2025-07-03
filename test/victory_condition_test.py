import unittest
from controller.jogo_controller import Jogo
from enuns.cor import Cor

class TestVictoryCondition(unittest.TestCase):

    def setUp(self):
        """
        Configura o ambiente para cada teste, garantindo que o estado do jogo
        seja resetado. Este método é executado antes de cada método de teste.
        """
        # Reseta o singleton Jogo antes de cada teste para garantir isolamento
        Jogo._instancia = None
        self.jogo = Jogo.get_instancia()
        self.jogo.inicializar_jogo(num_jogadores=1)

    def test_vitoria_erradicando_todas_as_doencas(self):
        """
        Testa se o jogo termina em vitória quando todas as doenças são erradicadas do tabuleiro.
        """
        # Garante que o jogo não comece com vitória (já que doenças são espalhadas inicialmente)
        self.jogo.verificar_condicoes_finais()
        self.assertFalse(self.jogo.vitoria, "O jogo não deveria começar com uma condição de vitória.")

        # Zera os níveis de todas as doenças em todas as cidades
        for cidade in self.jogo.cidades.values():
            for cor in Cor:
                cidade.remover_toda_doenca_de_cor(cor)

        # Verifica a condição de vitória novamente
        self.jogo.verificar_condicoes_finais()
        self.assertTrue(self.jogo.vitoria, "A vitória deveria ser declarada ao erradicar todas as doenças.")
        self.assertTrue(self.jogo.game_over, "O jogo deveria terminar após a vitória.")

    def test_vitoria_curando_todas_as_doencas(self):
        """
        Testa a condição de vitória original: curar todas as 4 doenças.
        """
        # Cura todas as doenças
        for cor in Cor:
            self.jogo.descobrir_cura(cor)

        # A verificação já é chamada dentro de descobrir_cura, mas verificamos o estado final
        self.assertTrue(self.jogo.vitoria, "A vitória deveria ser declarada ao curar todas as doenças.")
        self.assertTrue(self.jogo.game_over, "O jogo deveria terminar após a vitória.")

if __name__ == '__main__':
    unittest.main()
