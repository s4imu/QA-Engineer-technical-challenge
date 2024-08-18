import pytest

from pages.busca_correios_page import BuscaCorreiosPage

'''
Esse teste tem por objetivo realizar uma busca por CEP no site Busca CEP dos correios
'''

@pytest.mark.parametrize('setup_teardown', ["https://buscacepinter.correios.com.br/app/endereco/index.php"], indirect=True)

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.correios
class TestCT01Correios:
    def test_ct01_buscar_por_cep(self):
        CEP = "69005-040"
        tipo_cep = "ALL"
        correios_busca_page = BuscaCorreiosPage()


        correios_busca_page.realizar_busca(CEP, tipo_cep)
        correios_busca_page.verificar_busca_realizada()
