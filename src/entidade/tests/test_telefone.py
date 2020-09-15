from django.test import TestCase, Client
from rest_framework import status

from entidade.models import Telefone, Entidade
from utilitario.validadores import Validador


validador = Validador()
client = Client()

class TelefoneClass(TestCase):
    def setUp(self):
        self.entidade = Entidade.objects.create(
            nome='Teste Telefone',
            cpf_cnpj=validador.gerador_cpf(),
            cliente=True,
            fornecedor=False,
        )

        self.telefone_numero_invalido_brasil = {
            'entidade': 1,
            'codigo_pais': '55',
            'ddd': '21',
            'numero': '123456',
            'ramal': '',
        }

    def test_cadastro_telefone_numero_invalido_brasil(self):
        response = client.post(
            '/api/cadastros/telefones/',
            self.telefone_numero_invalido_brasil,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)