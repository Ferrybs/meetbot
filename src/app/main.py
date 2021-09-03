from modules.concrete.concreteStrategyMeetSelenium import ConcreteStrategyMeetSelenium

from modules.context.contextMeet import ContextMeet

if __name__ == "__main__":

    context_meet = ContextMeet(ConcreteStrategyMeetSelenium())
    res = context_meet.fazer_chamada()
    print(res)