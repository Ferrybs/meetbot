import time
from modules.selenium.selenium import Selenium

from modules.strategy.strategySend import StrategySend
from selenium.webdriver.chrome.webdriver import WebDriver

class ConcreteStrategySendSelenium(StrategySend):
    """
    """
    def __init__(self) -> None:
        self.drive:WebDriver
    
    def iniciar(self) -> None:
        self.driver = Selenium().set_driver()

    def fechar(self) -> None:
        self.driver.close()

    def send(self, text: str)-> str:
        try:
            time.sleep(1)
            self.iniciar()
        except Exception as e:
            print("Failed to open: ", e.args)
        try:
            time.sleep(2)
            self.driver.get("https://pastebin.com/")
            time.sleep(1)
            self.driver.find_element_by_xpath("//textarea[contains(@class,'textarea -form')]").send_keys(text)
            time.sleep(2)
            self.driver.find_elements_by_xpath("//button[@class='btn -big']")[0].click()
            time.sleep(5)
            link = self.driver.current_url
            self.fechar()
            return link
        except Exception as e:
            print("Failed to post:",e.args)