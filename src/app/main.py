from modules.concrete.concreteStrategySendSelenium import ConcreteStrategySendSelenium
from modules.context.contextSend import ContextSend
from modules.concrete.concreteStrategyMeetSelenium import ConcreteStrategyMeetSelenium

from modules.context.contextMeet import ContextMeet

if __name__ == "__main__":

    context_meet = ContextMeet(ConcreteStrategyMeetSelenium())
    res = context_meet.fazer_chamada()
    context_send = ContextSend(ConcreteStrategySendSelenium())
    link = context_send.enviar(res)
    context_meet.mensagem(link)
    print(link)