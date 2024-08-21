import pytest

from pages.busca_correios_page import BuscaCorreiosPage
from pages.trivago_busca_page import BuscaTrivagoPage

'''
Esse teste tem por objetivo realizar uma busca pelo termon Manaus no site da trivago
'''

@pytest.mark.parametrize('setup_teardown', ["https://www.trivago.com.br/"], indirect=True)

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.trivago
class TestCT01Correios:
    def test_ct01_buscar_por_cep(self):
        termo = "Manaus"
        opcao = "6"
        trivago_busca_page = BuscaTrivagoPage()

        trivago_busca_page.realizar_busca(termo)
        trivago_busca_page.ordenar_por_opcao(opcao)

        nome, nota, valor = trivago_busca_page.infos_1_elemento_lista()
        trivago_busca_page.gerar_resultado(nome,nota,valor)
        assert nome is not None and nota is not  None and valor is not None



