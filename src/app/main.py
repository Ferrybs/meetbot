from modules.concrete.concreteStrategyMeetSelenium import ConcreteStrategyMeetSelenium

from modules.context.contextMeet import ContextMeet

if __name__ == "__main__":

    context_meet = ContextMeet(ConcreteStrategyMeetSelenium())
    context_meet.abrir()
    res = context_meet.fazer_chamada()
    context_meet.fechar()
    print(res.keys())