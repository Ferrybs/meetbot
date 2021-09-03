from abc import ABC, abstractmethod


class StrategyRead(ABC):
    """
    """
    @abstractmethod
    def read(self) -> dict:
        pass