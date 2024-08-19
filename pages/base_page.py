import time

import conftest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select

class BasePage:
    def __init__(self):
        self.driver = conftest.driver
        self.page_title = (By.XPATH, "//span[@class='title']")
    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)

    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)

    def digitar(self, locator, text):
        self.encontrar_elemento(locator).send_keys(text)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()

    def checar_existencia_elemento(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(), f"Element '{locator}' not found!!!"

    def aguardar_elemento_aparecer(self, locator, timeout=10):
        return WebDriverWait(self.driver,  timeout).until(EC.presence_of_element_located(locator))

    def aguardar_elemento_desaparecer(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element(locator))

    def aguardar_resolver_captcha(self, timeout=13):
        self.driver.execute_script("alert('Clique no Botão OK para fechar esse Alerta e Preencha Corretamente o CAPTCHA (Não é necessário pressionar a tecla Enter após preenchimento) em 10 segundos');")
        return time.sleep(timeout)

    def selecionar_opcao_select(self, locator, option):
        dropdown = Select(self.encontrar_elemento(locator))
        return dropdown.select_by_value(option)
