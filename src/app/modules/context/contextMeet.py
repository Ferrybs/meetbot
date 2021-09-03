
from modules.strategy.strategyMeet import StrategyMeet


class ContextMeet():
    """
    """
    def __init__(self,strategy:StrategyMeet) -> None:

        self._strategy = strategy
        pass


    @property
    def strategy(self) -> StrategyMeet:
        return self._strategy


    @strategy.setter
    def strategy(self,strategy:StrategyMeet) -> None:
        self.strategy = strategy


    def fazer_chamada(self) -> dict:
        inciando = "Iniciando chamada: Digite qualquer coisa para contar presença!"
        terminando = "Chamada finalizada!"
        self.strategy.mensagem(inciando)
        input("Digite qualquer coisa para finalizar...")
        resultado = self.strategy.chamada()
        self.strategy.mensagem(terminando)
        return resultado
    def fechar(self)->None:
        self.strategy.fechar()
    def abrir(self)->None:
        self.strategy.iniciar()
    
