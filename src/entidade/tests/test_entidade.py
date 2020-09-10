from django.test import TestCase, Client
from rest_framework import status

from ..models import Entidade
from utilitario import formatadores
from utilitario.validadores import Validador


client = Client()
validador = Validador()


class EntidadeTest(TestCase):
    def setUp(self) -> None:
        self.entidade_cpf_valido = {
            'nome': 'CPF Valido',
            'cpf_cnpj': validador.gerador_cpf(),
            'cliente': True,
            'fornecedor': False,
        }
        self.entidade_cnpj_valido = {
            'nome': 'CNPJ Valido',
            'cpf_cnpj': validador.gerador_cnpj(),
            'cliente': True,
            'fornecedor': False,
        }
        self.entidade_cpf_invalido = {
            'nome': 'CPF Invalido',
            'cpf_cnpj': '12345678906',
            'cliente': True,
            'fornecedor': False,
        }
        self.entidade_cnpj_invalido = {
            'nome': 'CNPJ Invalido',
            'cpf_cnpj': '14891765000143',
            'cliente': True,
            'fornecedor': False,
        }

    def test_cadastro_entidade_cpf_invalido(self):
        nome_entidade = self.entidade_cpf_invalido.get('nome')
        cpf_entidade = self.entidade_cpf_invalido.get('cpf_cnpj')
        response = client.post(
            '/api/cadastros/entidades/',
            self.entidade_cpf_invalido,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data[0], f'CPF/CNPJ Inválido: {cpf_entidade}')
        self.assertFalse(Entidade.objects.filter(nome=nome_entidade))

    def test_cadastro_entidade_cnpj_invalido(self):
        nome_entidade = self.entidade_cnpj_invalido.get('nome')
        cnpj_entidade = self.entidade_cnpj_invalido.get('cpf_cnpj')
        response = client.post(
            '/api/cadastros/entidades/',
            self.entidade_cnpj_invalido,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data[0], f'CPF/CNPJ Inválido: {cnpj_entidade}')
        self.assertFalse(Entidade.objects.filter(nome=nome_entidade))
