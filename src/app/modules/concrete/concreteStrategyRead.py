import json

from modules.strategy.strategyRead import StrategyRead
class ConcreteStrategyRead(StrategyRead):
    """
    """
    def read(self)-> dict:
        try:
            with open('docs/auth.json', 'r') as json_file:
                dados = json.load(json_file)
            
            return dados
        except:
            print("Failed to load auth.json")
        pass