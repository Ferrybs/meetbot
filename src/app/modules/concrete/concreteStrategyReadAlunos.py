import json

from modules.strategy.strategyRead import StrategyRead

class ConcreteStrategyReadAluno(StrategyRead):
    """
    """
    def read(self)-> list:
        try:
            f = open("docs/alunos.txt","r")
            dados = f.read().split(", ")
            
            return dados
        except:
            print("Failed to load auth.json")
        pass