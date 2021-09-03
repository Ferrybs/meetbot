
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
        try:
            self.strategy.iniciar()
            inciando = "Iniciando chamada: Digite qualquer coisa para contar presença!"
            terminando = "Chamada finalizada!"
            self.strategy.mensagem(inciando)
            input("Digite qualquer coisa para finalizar...")
            resultado = self.strategy.chamada()
            self.strategy.mensagem(terminando)
            self.strategy.fechar()
            return resultado
        except Exception as e:
            print("Failed to fazer chamada: ", e.args)

    def mensagem(self,text: str) ->None:
        try:
            self.strategy.iniciar()
            self.strategy.mensagem("Chamada post: "+ text)
            self.strategy.fechar()
        except Exception as e:
            print("Failed to mensagem: ", e.args)
        pass
    
