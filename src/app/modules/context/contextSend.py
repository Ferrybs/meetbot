
from modules.strategy.strategySend import StrategySend


class ContextSend():
    """
    """
    def __init__(self,strategy:StrategySend) -> None:
        self._strategy = strategy
        pass

    @property
    def strategy(self) -> StrategySend:
        return self._strategy


    @strategy.setter
    def strategy(self,strategy:StrategySend) -> None:
        self._strategy = strategy
        return

    def enviar(self, presentes: list) -> str:
        try:
            presentes.sort()
            resultado = '\n'.join(presentes)
            return self.strategy.send(resultado)
        except Exception as e:
            print("Failed to post: ", e.args)
        pass
