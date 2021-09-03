
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

    def enviar(self, presentes: dict) -> str:
        try:
            text = '\n'.join(list(presentes.keys()))
            return self.strategy.send(text)
        except Exception as e:
            print("Failed to post: ", e.args)
        pass
