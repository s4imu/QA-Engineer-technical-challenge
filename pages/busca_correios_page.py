import time
from tkinter.tix import Select

import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BuscaCorreiosPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.campo_busca = (By.ID, "endereco")
        self.campo_tipo_cep = (By.ID, "tipoCEP")
        self.campo_captcha = (By.ID, "captcha")
        self.btn_buscar = (By.ID, "btn_pesquisar")
        self.titulo_pagina_busca = (By.XPATH, "//h5[text()='Resultado da Busca por Endereço ou CEP']")

    def realizar_busca(self, termo_busca, tipo_cep):
        self.type(self.campo_busca, termo_busca)
        self.select_option(self.campo_tipo_cep, tipo_cep)
        self.click(self.campo_captcha)
        self.wait_resolve_captcha()
        self.click(self.btn_buscar)

    def verificar_busca_realizada(self):
        self.check_if_element_exists(self.titulo_pagina_busca)





