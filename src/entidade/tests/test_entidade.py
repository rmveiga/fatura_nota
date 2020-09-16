from django.test import TestCase, Client
from rest_framework import status

from ..models import Entidade
from utilitario.validadores import Validador

client = Client()
validador = Validador()


class EntidadeTest(TestCase):
    def setUp(self) -> None:
        self.entidade_cpf_valido = Entidade.objects.create(
            nome='CPF Valido',
            cpf_cnpj=validador.gerador_cpf(),
            cliente=True,
            fornecedor=False,
        )
        self.entidade_cnpj_valido = Entidade.objects.create(
            nome='CNPJ Valido',
            cpf_cnpj=validador.gerador_cnpj(),
            cliente=True,
            fornecedor=False,
        )
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
        response = client.post(
            '/api/cadastros/entidades/',
            self.entidade_cpf_invalido,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(Entidade.objects.filter(nome=nome_entidade))

    def test_edicao_entidade_cpf_invalido(self):
        id_entidade = self.entidade_cpf_valido.pk
        cpf_valido = self.entidade_cpf_valido.cpf_cnpj
        cpf_invalido = self.entidade_cpf_invalido.get('cpf_cnpj')
        content = {'cpf_cnpj': cpf_invalido}

        response = client.patch(
            f'/api/cadastros/entidades/{id_entidade}/',
            content,
            content_type='application/json'
        )

        entidade = Entidade.objects.get(pk=id_entidade)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(entidade.cpf_cnpj, cpf_valido)

    def test_cadastro_entidade_cnpj_invalido(self):
        nome_entidade = self.entidade_cnpj_invalido.get('nome')
        response = client.post(
            '/api/cadastros/entidades/',
            self.entidade_cnpj_invalido,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(Entidade.objects.filter(nome=nome_entidade))

    def test_edicao_entidade_cnpj_invalido(self):
        id_entidade = self.entidade_cnpj_valido.pk
        cnpj_valido = self.entidade_cnpj_valido.cpf_cnpj
        cnpj_invalido = self.entidade_cnpj_invalido.get('cpf_cnpj')
        content = {'cpf_cnpj': cnpj_invalido}

        response = client.patch(
            f'/api/cadastros/entidades/{id_entidade}/',
            content,
            content_type='application/json'
        )

        entidade = Entidade.objects.get(pk=id_entidade)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(entidade.cpf_cnpj, cnpj_valido)

    def test_cadastro_entidade_nao_cliente_e_nao_fornecedor(self):
        nome_entidade = self.entidade_nao_cliente_e_nao_fornecedor.get('nome')
        response = client.post(
            '/api/cadastros/entidades/',
            self.entidade_nao_cliente_e_nao_fornecedor,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(Entidade.objects.filter(nome=nome_entidade))

    def test_edicao_entidade_nao_cliente_e_nao_fornecedor(self):
        id_entidade = self.entidade_cpf_valido.pk
        cliente_entidade = self.entidade_cpf_valido.cliente
        content = {
            'cliente': False,
            'fornecedor': False,
        }

        response = client.patch(
            f'/api/cadastros/entidades/{id_entidade}/',
            content,
            content_type='application/json'
        )

        entidade = Entidade.objects.get(pk=id_entidade)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(entidade.cliente, cliente_entidade)
