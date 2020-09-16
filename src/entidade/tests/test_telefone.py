from django.test import TestCase, Client
from rest_framework import status

from entidade.models import Telefone, Entidade
from utilitario.validadores import Validador

validador = Validador()
client = Client()


class TelefoneTest(TestCase):
    def setUp(self):
        self.entidade = Entidade.objects.create(
            nome='Teste Telefone',
            cpf_cnpj=validador.gerador_cpf(),
            cliente=True,
            fornecedor=False,
        )
        self.telefone = Telefone.objects.create(
            entidade=self.entidade,
            codigo_pais='55',
            ddd='21',
            numero='999999999',
            ramal='',
        )

        self.telefone_numero_invalido_brasil = {
            'entidade': 1,
            'codigo_pais': '55',
            'ddd': '21',
            'numero': '123456',
            'ramal': '',
        }
        self.telefone_ddd_invalido_brasil = {
            'entidade': 1,
            'codigo_pais': '55',
            'ddd': '01',
            'numero': '999999999',
            'ramal': '',
        }

    def test_cadastro_telefone_numero_invalido_brasil(self):
        response = client.post(
            '/api/cadastros/telefones/',
            self.telefone_numero_invalido_brasil,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_edicao_telefone_numero_invalido_brasil(self):
        id_telefone = self.telefone.pk
        id_entidade = self.telefone.entidade.pk
        numero_telefone = self.telefone.numero
        content = {
            'entidade': id_entidade,
            'codigo_pais': '55',
            'ddd': '21',
            'numero': '1234567',
        }
        response = client.patch(
            f'/api/cadastros/telefones/{id_telefone}/',
            content,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        telefone = Telefone.objects.get(pk=id_telefone)
        self.assertEqual(telefone.numero, numero_telefone)

    def test_cadastro_telefone_ddd_invalido_brasil(self):
        response = client.post(
            '/api/cadastros/telefones/',
            self.telefone_ddd_invalido_brasil,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_edicao_telefone_ddd_invalido_brasil(self):
        id_telefone = self.telefone.pk
        id_entidade = self.telefone.entidade.pk
        ddd_telefone = self.telefone.ddd
        content = {
            'entidade': id_entidade,
            'codigo_pais': '55',
            'ddd': '01',
            'numero': '999999999',
        }
        response = client.patch(
            f'/api/cadastros/telefones/{id_telefone}/',
            content,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        telefone = Telefone.objects.get(pk=id_telefone)
        self.assertEqual(telefone.ddd, ddd_telefone)
