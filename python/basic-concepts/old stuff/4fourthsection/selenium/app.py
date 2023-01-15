#pip install selenium, caso o selenium não esteja instalado

#cada chrome driver tem uma versão compativel com o chrome instalado no pc
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class ChromeAuto:
    #usado para abrir o chrome, configurações iniciais
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('chromedriver.exe') #local onde fica o CHROMEDRIVER , interface que junta chrome ao selenium
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options= self.options
        )

    # a partir de agora, depende do site que queremos entrar;

    def acessa_site(self,site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clica_menu_traco(self):
        try:
            btn_menu = self.chrome.find_element(By.CLASS_NAME, "btn-link")
            btn_menu.click()
        except Exception as e:
            print('Erro ao clicar no botão menu:', e)

    def clica_sign_in(self):
        try:
            btn_sign = self.chrome.find_element(By.LINK_TEXT, "Sign in")
            btn_sign.click()
        except Exception as error:
            print('Erro ao clicar no botão sign in:', e)

    def faz_login(self):
        try:
            input_login = self.chrome.find_element(By.ID, 'login_field')
            input_password = self.chrome.find_element(By.ID, 'password')
            input_login.send_keys('')#EMAIL
            input_password.send_keys('')#SENHA
            btn_login = self.chrome.find_element(By.NAME, 'commit')
            btn_login.click()
        except Exception as e:
            print('erro ao fazer login', e)

    def click_perfil(self):
        try:
            perfil = self.chrome.find_element(By.CSS_SELECTOR,'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary > img')
            perfil.click()
        except Exception as e:
            print('erro ao clicar no perfil',e)

    def verifica_usuario(self, usuario):
        profile_l

    def faz_logout(self):
        try:
            logout = self.chrome.find_element(By.CSS_SELECTOR, 'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
            logout.click()
        except Exception as e:
            print('erro ao clicar no logout', e)



if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa_site('https://github.com')


    chrome.clica_menu_traco()
    chrome.clica_sign_in()
    chrome.faz_login()
    chrome.click_perfil()
    sleep(10)
    chrome.faz_logout()
    sleep(10)
    chrome.sair()