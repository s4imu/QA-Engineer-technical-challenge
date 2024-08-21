import pytest

from pages.busca_correios_page import BuscaCorreiosPage

'''
Esse teste tem por objetivo realizar uma busca pelo termo "Lojas Bemol" no site Busca CEP dos correios
'''

@pytest.mark.parametrize('setup_teardown', ["https://buscacepinter.correios.com.br/app/endereco/index.php"], indirect=True)

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.correios
class TestCT02Correios:
    def test_ct02_buscar_por_termo(self):
        termo = "Lojas Bemol"
        tipo_cep = "ALL"
        correios_busca_page = BuscaCorreiosPage()
        campo_resultado = correios_busca_page.campo_logadouro_resultado

        correios_busca_page.realizar_busca(termo, tipo_cep)
        correios_busca_page.verificar_busca_realizada(campo_resultado, termo)
