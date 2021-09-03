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
    @abstractmethod
    def iniciar(self) -> None:
        pass
    @abstractmethod
    def fechar(self) -> None:
        pass