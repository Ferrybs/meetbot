from modules.concrete.concreteStrategyReadAlunos import ConcreteStrategyReadAluno
from modules.context.contextRead import ContextRead
from modules.concrete.concreteStrategySendSelenium import ConcreteStrategySendSelenium
from modules.context.contextSend import ContextSend
from modules.concrete.concreteStrategyMeetSelenium import ConcreteStrategyMeetSelenium

from modules.context.contextMeet import ContextMeet

def rambim():
    context_meet = ContextMeet(ConcreteStrategyMeetSelenium())
    context_send = ContextSend(ConcreteStrategySendSelenium())
    context_read = ContextRead(ConcreteStrategyReadAluno())
    alunos = context_read.read()
    presentes = context_meet.fazer_chamada()
    ausentes = list(set(alunos.keys()) - set(presentes.keys()))
    link = context_send.enviar(ausentes)
    context_meet.mensagem(link)

def menu():
    op =1
    while(op!=0):
        print("\nCHAMADA")
        print("1- Fazer chamada e postar")
        print("0 - Sair")
        op = int(input("Digite o desejado: "))
        if op ==1:
            rambim()
        else:
            print("Saindo...")
            op=0


if __name__ == "__main__":
    menu()