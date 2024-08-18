import os

import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BuscaTrivagoPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.campo_busca = (By.ID, "input-auto-complete")
        self.escolha_submenu = (By.XPATH, "//span[@data-testid='suggestion-subtitle' and text()='Cidade · Amazonas, Brasil']")
        self.btn_pesquisar = (By.XPATH, "//span[text()='Pesquisar']")
        self.select_ordenar_por = (By.ID, "sorting-selector")
        self.lista_nome_acomodacoes = (By.XPATH, "//span[@itemprop='name']")
        self.lista_notas_acomodacoes = (By.XPATH, "//span[@itemprop='ratingValue']")
        self.lista_valores_acomodacoes = (By.XPATH, "//b[contains(text(),'R$')]")

    def realizar_busca(self, termo_busca):
        self.type(self.campo_busca, termo_busca)
        self.wait_element_appears(self.escolha_submenu)
        self.click(self.escolha_submenu)
        self.wait_element_disappear(self.escolha_submenu)
        self.click(self.btn_pesquisar)

    def ordenar_por_opcao(self, opcao):
        self.wait_element_appears(self.select_ordenar_por)
        self.select_option(self.select_ordenar_por, opcao)

    def valor_propriedade_do_1_elemento(self, locator):
        self.wait_element_appears(locator)
        lista_valores = self.find_elements(locator)
        return lista_valores[0].text

    def infos_1_elemento_lista(self):
        nome_primeiro_elemento = self.valor_propriedade_do_1_elemento(self.lista_nome_acomodacoes)
        nota_primeiro_elemento = self.valor_propriedade_do_1_elemento(self.lista_notas_acomodacoes)
        valor_primeiro_elemento = self.valor_propriedade_do_1_elemento(self.lista_valores_acomodacoes)
        return nome_primeiro_elemento, nota_primeiro_elemento, valor_primeiro_elemento

    @staticmethod
    def gerar_resultado(nome, nota, valor):
        with open('test_ct03_trivago_buscar_por_termo_results.txt', 'w') as file:
            file.write("Nome da 1ª acomodação da lista: {} \nNota da 1ª acomodação da lista: {} \nValor da 1ª acomodação da lista: {} \n".format(nome, nota, valor))