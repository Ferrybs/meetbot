import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from modules.concrete.concreteStrategyReadWin import ConcreteStrategyReadWin
from modules.concrete.concreteStrategyRead import ConcreteStrategyRead

from modules.context.contextRead import ContextRead


class SeleniumSetup():
    """
    """
    def __init__(self) -> None:
        self.driver: WebDriver
        self.context_read: ContextRead= ContextRead(ConcreteStrategyRead())
        self.meet: str
        self.path: str

    def start(self)->WebDriver:
        try:
            self.set_driver()
            self.login()
            self.joinMeet()
            return self.driver
        except Exception as e:
            print("Failed to start: ",e.args)

    def stop(self)-> None:
        try:
            self.driver.close()
        except Exception as e:
            print("Failed to stop: ",e.args)
        pass

    def set_driver(self) -> WebDriver:
        driver:WebDriver
        auth = self.context_read.read()
        self.meet = auth.get("meet")
        self.path = auth.get("path")
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-infobars")
            options.add_argument("--remote-debugging-port=9222")  # this
            options.add_argument('--start-maximized')
            options.add_argument("--mute-audio")
            options.add_argument("--user-data-dir="+ self.path)

            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.add_experimental_option("prefs", { \
            "profile.default_content_setting_values.media_stream_mic": 2,     # 1:allow, 2:block
            "profile.default_content_setting_values.media_stream_camera": 2,
            "profile.default_content_setting_values.notifications": 2
            })

            driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
        except Exception as e:
            print("Faied to start WebDriver: ",e.args)
            
        self.driver = driver

    def login(self)->None:
        try:
            self.driver.get(r'https://google.com')
            self.driver.implicitly_wait(5)

            cookies = self.driver.get_cookies()
            key = "google"
            for cookie in cookies:
                #print(cookie)
                if key in cookie['domain']: 
                    print('Login Successful...!!')
                    return
            
            op = input("Esperando login...")
            print('Login Successful...!!')
        except Exception as e:
            print("Failed login: ",e.args)
    
    def joinMeet(self)->None:
        try:
            auth = self.context_read.read()
            self.meet = auth.get("meet")
            time.sleep(2)
            self.driver.get(self.meet)
            print("Get Successful...:" + self.meet)
            time.sleep(2)
        except Exception as e:
            print("Join Failed: ",e.args)
        
        try:
            self.driver.implicitly_wait(3)
            element = self.driver.find_element_by_xpath("//div[@class='I5fjHe wb61gb']")
            self.driver.execute_script("arguments[0].click();", element)
            element = self.driver.find_element_by_xpath("(//div[@class='I5fjHe wb61gb'])[2]")
            self.driver.execute_script("arguments[0].click();", element)
            print("Click Successful...")
        except Exception as e:
            print("Click Failed: ",e.args)
        try:
            self.driver.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Join now' )]").click()
            print("Join Successful...")
        except:
            try:
                self.driver.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Ask to join')]").click()
                print("Join Successful...")
            except:
                try:
                    self.driver.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Participar agora')]").click()
                    print("Join Successful...")
                except:
                    try:
                        self.driver.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Pedir para participar')]").click()
                        try:
                            #LEMBRAR DE CLICAR NA GRAVACAO SENDO GRAVADA
                            self.driver.implicitly_wait(3)
                            time.sleep(2)
                            element = self.driver.find_element_by_class_name('CwaK9')
                            self.driver.execute_script("arguments[0].click();", element)
                        except:
                            print("Failed to Click on chamada gravada...")

                        print("Join Successful...")
                    except Exception as e:
                        print("Join Failed: ",e.args)