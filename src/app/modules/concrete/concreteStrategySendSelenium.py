import time
from modules.selenium.seleniumSetup import SeleniumSetup

from modules.strategy.strategySend import StrategySend
from selenium.webdriver.chrome.webdriver import WebDriver

class ConcreteStrategySendSelenium(StrategySend):
    """
    """
    def __init__(self) -> None:
        self.drive:WebDriver
    
    def iniciar(self) -> None:
        self.driver = SeleniumSetup().set_driver()

    def fechar(self) -> None:
        self.driver.close()

    def send(self, text: str)-> str:
        try:
            time.sleep(1)
            self.iniciar()
        except Exception as e:
            print("Failed to open: ", e.args)
        try:
            i = 4
            while(i!=1):
                time.sleep(2)
                self.driver.get("https://www.heypasteit.com/")
                time.sleep(1)
                self.driver.find_element_by_css_selector("textarea#text").send_keys(text)
                time.sleep(2)
                self.driver.find_elements_by_class_name("btnStyle")[1].click()
                time.sleep(5)
                result = self.driver.find_element_by_class_name("info").text[15:22]
                result = result.strip()
                if(result == "error"):
                    i= i -1
                else:
                    i = 1
            
            link = "https://www.heypasteit.com/clip/" + result
            self.fechar()
            return link
        except Exception as e:
            print("Failed to post:",e.args)