from abc import ABC, abstractmethod


class StrategySend(ABC):
    """
    """
    @abstractmethod
    def iniciar(self) -> None:
        pass
    @abstractmethod
    def fechar(self) -> None:
        pass
    @abstractmethod
    def send(self, text: str) -> str:
        pass