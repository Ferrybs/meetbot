import json

from modules.strategy.strategyRead import StrategyRead
class ConcreteStrategyReadWin(StrategyRead):
    """
    """
    def read(self)-> dict:
        try:
            with open('C:/Users/portr/Documents/meetbot/docs/auth.json', 'r') as json_file:
                dados = json.load(json_file)
            
            return dados
        except:
            print("Failed to load auth.json")
        pass