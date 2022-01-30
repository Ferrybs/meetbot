from modules.strategy.strategyRead import StrategyRead

class ConcreteStrategyReadAlunoWin(StrategyRead):
    """
    """
    def read(self)-> dict:
        try:
            f = open("C:/Users/portr/Documents/meetbot/docs/alunos.txt","r")
            alunos = f.read().split("\n")

            dados = dict.fromkeys(alunos,1)

            return dados
        except:
            print("Failed to load auth.json")
        pass