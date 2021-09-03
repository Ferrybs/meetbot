from abc import ABC, abstractmethod


class StrategyMeet(ABC):
    """
    """
    @abstractmethod
    def mensagem(self,text:str) -> None:
        pass
    @abstractmethod
    def chamada(self) -> dict:
        pass