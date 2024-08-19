import time

import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BuscaCorreiosPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.campo_busca = (By.ID, "endereco")
        self.select_tipo_cep = (By.ID, "tipoCEP")
        self.campo_captcha = (By.ID, "captcha")
        self.btn_buscar = (By.ID, "btn_pesquisar")
        self.campo_cep_resultado = (By.XPATH, "//td[@data-th='CEP']")
        self.campo_logadouro_resultado = (By.XPATH, "//td[@data-th='Logradouro/Nome']")

    def realizar_busca(self, termo_busca, tipo_cep):
        self.digitar(self.campo_busca, termo_busca)
        self.selecionar_opcao_select(self.select_tipo_cep, tipo_cep)
        self.clicar(self.campo_captcha)
        self.aguardar_resolver_captcha()
        self.clicar(self.btn_buscar)

    def verificar_busca_realizada(self, locator, valor_esperado):
        self.aguardar_elemento_aparecer(locator)
        elemento = self.encontrar_elemento(locator)
        assert valor_esperado in elemento.text, f"O texto '{elemento.text}' não contém a resposta esperada '{valor_esperado}'"





