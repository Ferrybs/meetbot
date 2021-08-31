import json
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

def login(driver: WebDriver,gmailId:str,passWord: str ):

    try:
        driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
        'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
        '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
        driver.implicitly_wait(5)
    
        loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
        loginBox.send_keys(gmailId)
    
        nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
        nextButton[0].click()
    
        passWordBox = driver.find_element_by_xpath(
            '//*[@id ="password"]/div[1]/div / div[1]/input')
        passWordBox.send_keys(passWord)
    
        nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
        nextButton[0].click()
    
        print('Login Successful...!!')
    except:
        cookies = driver.get_cookies()
        key = "mail.google.com"
        for cookie in cookies:
            if cookie['domain'] == key: 
                print('Login Successful...!!')
                return

        print('Login Failed')

def joinMeet(driver: WebDriver, meet: str):
    try:
        time.sleep(2)
        driver.get(meet)
        print("Get Successful...")
    except:
        print("Join Failed")

    try:
        driver.implicitly_wait(3)
        element = driver.find_element_by_class_name('CwaK9')
        driver.execute_script("arguments[0].click();", element)
        print("Click Successful...")
    except:
        print("Click Failed")
    try:
        driver.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Join now' )]").click()
        print("Join Successful...")
    except:
        try:
            driver.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Ask to join')]").click()
            print("Join Successful...")
        except:
            try:
                driver.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Participar agora')]").click()
                print("Join Successful...")
            except:
                try:
                    driver.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Pedir para participar')]").click()
                    print("Join Successful...")
                except:
                    print("Join Failed")

def avisoChamada(driver: WebDriver, texto: str):
    print("Aviso chamada...: " + texto)
    try:
        time.sleep(3)
        #BOTAO ABRIR CHAT
        botao = driver.find_elements_by_class_name("r6xAKc")
        botao[2].click()
    except:
        print("Failed to open chat")

    try:
        time.sleep(3)
        chamada = driver.find_element_by_xpath("//textarea[@class='KHxj8b tL9Q4c']")
        chamada.send_keys(texto)
        time.sleep(1)
        chamada.send_keys(Keys.ENTER)
        time.sleep(4)
        botao[2].click()
    except:
        print("Failed to send: " + texto)
    

    


def alunosConectados(driver: WebDriver):
    lista = []
    try:
        time.sleep(2)
        #BOTAO ABRIR CONECTADOS
        botao = driver.find_elements_by_class_name("r6xAKc")
        botao[1].click()
    except:
        print("Failed to open connected")
    try:
        time.sleep(2)
        conectados = driver.find_elements_by_class_name("ZjFb7c")
        for i in conectados:
            lista.append(i.text)
        time.sleep(2)
        lista.remove('Chamada Meet')
        lista.sort()
        botao[1].click()
    except:
        print("Failed to find connected")
    
    return lista

def chamada(driver: WebDriver):
    try:
        time.sleep(2)
        #BOTAO ABRIR CHAT
        botao = driver.find_elements_by_class_name("r6xAKc")
        botao[2].click()
        time.sleep(3)
        aluno = driver.find_elements_by_class_name("YTbUzc")
        
        presentes = []
        for i in aluno:
            presentes.append(i.text)
        print(presentes)
        presentes.remove("Você")
        time.sleep(3)
        botao[2].click()
    except:
        print("Failed to find names")

    
    return presentes

def fazerChamada(driver: WebDriver):
    avisoChamada(driver, "Iniciando chamada:")
    input("Digite qualquer tecla para terminar a chamada...")
    resp = chamada(driver)
    time.sleep(2)
    avisoChamada(driver,"Chamada finalizada:")
    return resp


def setDriver():
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=selenium") 
    options.add_argument("--disable-infobars")
    options.add_argument("--window-size=800,600")
    options.add_argument("--mute-audio")

    options.add_experimental_option("prefs", { \
      "profile.default_content_setting_values.media_stream_mic": 2,     # 1:allow, 2:block
      "profile.default_content_setting_values.media_stream_camera": 2,
       "profile.default_content_setting_values.notifications": 2
    })
    return webdriver.Chrome(ChromeDriverManager().install(),options=options)

def menu(driver: WebDriver,gmailId:str,passWord: str, meet: str ):
    op=1
    conectados = []
    presentes = []
    ausentes = []
    while(op != 0):
        print("\t CHAMADA MEET")
        print("1 - Entrar no meet")
        print("2 - Fazer chamada")
        print("3 - Alunos conectados")
        print("4 - Alunos presentes")
        print("5 - Alunos conectados ausentes")
        print("0 - Sair")

        op = int(input("Escolher:"))

        if op == 1:
            login(driver,gmailId,passWord)
            joinMeet(driver,meet)
        elif op == 2:
            presentes = fazerChamada(driver)
        elif op == 3:
            driver.implicitly_wait(5)
            conectados = alunosConectados(driver)
            conectados.sort
            print("-"*25)
            print("Alunos conectados:")
            for i in conectados:
                print(i)
            print("-"*25)
        elif op == 4:
            print("-"*25)
            print("Alunos presentes:")
            for i in presentes:
                print(i)
            print("-"*25)
        elif op == 5:
            ausentes = list(set(conectados)-set(presentes))
            print("-"*25)
            print("Alunos conectados ausentes:")
            for i in ausentes:
                print(i)
            ausentes.clear()
            print("-"*25)
        else:
            driver.close()
            print("Saindo...")

if __name__ == "__main__":

    try:
        driver = setDriver()
    except:
        print("Failed to open driver")
    try:
        with open('auth.json', 'r') as json_file:
            dados = json.load(json_file)

        gmailId = dados.get("email")
        passWord = dados.get("password")
        meet = dados.get("meet")
        menu(driver,gmailId,passWord,meet)
    except:
        print("Failed to load login.json")


    


    


