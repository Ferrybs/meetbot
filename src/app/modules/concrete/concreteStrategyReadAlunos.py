import json

from modules.strategy.strategyRead import StrategyRead

class ConcreteStrategyReadAluno(StrategyRead):
    """
    """
    def read(self)-> dict:
        try:
            f = open("docs/alunos.txt","r")
            alunos = f.read().split(", ")

            dados = dict.fromkeys(alunos,1)

            return dados
        except:
            print("Failed to load auth.json")
        pass