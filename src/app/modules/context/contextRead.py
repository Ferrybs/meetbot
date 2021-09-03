from modules.strategy.strategyRead import StrategyRead


class ContextRead():
    """
    """
    def __init__(self,strategy:StrategyRead) -> None:
        self._strategy = strategy
        pass

    @property
    def strategy(self) -> StrategyRead:
        return self._strategy


    @strategy.setter
    def strategy(self,strategy:StrategyRead) -> None:
        self.strategy = strategy
        return

    def read(self) -> dict:
        return self.strategy.read()
