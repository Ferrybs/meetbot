from logging import exception
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver

from modules.selenium.selenium import Selenium
from modules.strategy.strategyMeet import StrategyMeet


class ConcreteStrategyMeetSelenium(StrategyMeet):
    def __init__(self) -> None:
        self.driver:WebDriver = Selenium().start()

    def start(self)-> None:
        self.driver = Selenium().start()
        pass

    def stop(self)-> None:
        try:
            self.driver.close()
        except Exception as e:
            print("Failed to stop: ", e.args)
        pass
    

    def mensagem(self,text: str) -> None:
        try:
            time.sleep(3)
            #BOTAO ABRIR CHAT
            botao = self.driver.find_elements_by_class_name("r6xAKc")
            botao[2].click()
        except Exception as e:
            print("Failed to open chat: ", e.args)

        try:
            time.sleep(3)
            chamada = self.driver.find_element_by_xpath("//textarea[@class='KHxj8b tL9Q4c']")
            chamada.send_keys(text)
            time.sleep(1)
            chamada.send_keys(Keys.ENTER)
            time.sleep(4)
            botao[2].click()
        except Exception as e:
            print("Failed to send message: ", e.args)


    def chamada(self) -> dict:
        try:
            time.sleep(2)
            #BOTAO ABRIR CHAT
            botao = self.driver.find_elements_by_class_name("r6xAKc")
            botao[2].click()
            time.sleep(3)
            aluno = self.driver.find_elements_by_class_name("YTbUzc")
            
            presentes = {}
            for i in aluno:
                presentes[i.text] = 1
            presentes.pop('Você')

            time.sleep(3)
            botao[2].click()

            return presentes
        except Exception as e:
            print("Failed to find names: ", e.args)