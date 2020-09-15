from django.test import TestCase, Client
from rest_framework import status

from ..models import Entidade
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
        self.entidade_nao_cliente_e_nao_fornecedor = {
            'nome': 'Não cliente e não fornecedor',
            'cpf_cnpj': validador.gerador_cpf(),
            'cliente': False,
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
        self.assertEqual(response.data.get('cpf_cnpj')[0], f'CPF/CNPJ Inválido: {cpf_entidade}')
        self.assertFalse(Entidade.objects.filter(nome=nome_entidade))

    def test_edicao_entidade_cpf_invalido(self):
        response = client.post(
            '/api/cadastros/entidades/',
            self.entidade_cpf_valido,
            content_type='application/json'
        )

        id_entidade = response.data.get('id')
        cpf_valido = response.data.get('cpf_cnpj')
        cpf_invalido = self.entidade_cpf_invalido.get('cpf_cnpj')
        content = {'cpf_cnpj': cpf_invalido}

        response = client.patch(
            f'/api/cadastros/entidades/{id_entidade}/',
            content,
            content_type='application/json'
        )

        entidade = Entidade.objects.get(pk=id_entidade)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get('cpf_cnpj')[0], f'CPF/CNPJ Inválido: {cpf_invalido}')
        self.assertEqual(entidade.cpf_cnpj, cpf_valido)

    def test_cadastro_entidade_cnpj_invalido(self):
        nome_entidade = self.entidade_cnpj_invalido.get('nome')
        cnpj_entidade = self.entidade_cnpj_invalido.get('cpf_cnpj')
        response = client.post(
            '/api/cadastros/entidades/',
            self.entidade_cnpj_invalido,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get('cpf_cnpj')[0], f'CPF/CNPJ Inválido: {cnpj_entidade}')
        self.assertFalse(Entidade.objects.filter(nome=nome_entidade))

    def test_edicao_entidade_cnpj_invalido(self):
        response = client.post(
            '/api/cadastros/entidades/',
            self.entidade_cnpj_valido,
            content_type='application/json'
        )

        id_entidade = response.data.get('id')
        cnpj_valido = response.data.get('cpf_cnpj')
        cnpj_invalido = self.entidade_cnpj_invalido.get('cpf_cnpj')
        content = {'cpf_cnpj': cnpj_invalido}

        response = client.patch(
            f'/api/cadastros/entidades/{id_entidade}/',
            content,
            content_type='application/json'
        )

        entidade = Entidade.objects.get(pk=id_entidade)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get('cpf_cnpj')[0], f'CPF/CNPJ Inválido: {cnpj_invalido}')
        self.assertEqual(entidade.cpf_cnpj, cnpj_valido)

    def test_cadastro_entidade_nao_cliente_e_nao_fornecedor(self):
        nome_entidade = self.entidade_nao_cliente_e_nao_fornecedor.get('nome')
        response = client.post(
            '/api/cadastros/entidades/',
            self.entidade_nao_cliente_e_nao_fornecedor,
            content_type='application/json'
        )

        erro_esperado = 'A entidade precisa ser um cliente, fornecedor ou ambos'

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get('non_field_errors')[0], erro_esperado)
        self.assertFalse(Entidade.objects.filter(nome=nome_entidade))

    def test_edicao_entidade_nao_cliente_e_nao_fornecedor(self):
        response = client.post(
            '/api/cadastros/entidades/',
            self.entidade_cpf_valido,
            content_type='application/json'
        )

        id_entidade = response.data.get('id')
        content = {
            'cliente': False,
            'fornecedor': False,
        }

        response = client.patch(
            f'/api/cadastros/entidades/{id_entidade}/',
            content,
            content_type='application/json'
        )

        erro_esperado = 'A entidade precisa ser um cliente, fornecedor ou ambos'
        entidade = Entidade.objects.get(pk=id_entidade)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get('non_field_errors')[0], erro_esperado)
        self.assertTrue(entidade.cliente)