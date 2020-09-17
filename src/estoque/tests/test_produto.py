from django.test import TestCase, Client
from rest_framework import status

from estoque.models import Produto

client = Client()

class ProdutoTest(TestCase):
    def setUp(self) -> None:
        self.preco_venda_negativo = {
            'descricao': 'Preço de Venda Negativo',
            'preco_venda': -1,
        }
        self.produto_valido = Produto.objects.create(
            descricao='Produto Válido',
            preco_venda=1,
        )
        self.produto_bloqueado = Produto.objects.create(
            descricao='Produto Bloqueado',
            preco_venda=1,
            bloqueado=True,
        )

    def test_cadastro_produto_preco_venda_negativo(self):
        descricao_produto = self.preco_venda_negativo.get('descricao')
        response = client.post(
            '/api/estoque/produtos/',
            self.preco_venda_negativo,
            content_type='application/json',
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(Produto.objects.filter(descricao=descricao_produto))

    def test_edicao_produto_preco_venda_negativo(self):
        id_produto = self.produto_valido.pk
        preco_venda_produto = self.produto_valido.preco_venda
        content = {'preco_venda': -1}
        response = client.patch(
            f'/api/estoque/produtos/{id_produto}/',
            content,
            content_type='application/json',
        )

        produto = Produto.objects.get(pk=id_produto)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(produto.preco_venda, preco_venda_produto)

    def test_edicao_produto_bloqueado(self):
        id_produto = self.produto_bloqueado.pk
        descricao_produto = self.produto_bloqueado.descricao
        preco_venda_produto = self.produto_bloqueado.preco_venda
        content = {
            'descricao': 'Nova Descrição',
            'preco_venda': 100,
        }

        response = client.patch(
            f'/api/estoque/produtos/{id_produto}/',
            content,
            content_type='application/json',
        )

        produto = Produto.objects.get(pk=id_produto)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(produto.descricao, descricao_produto)
        self.assertEqual(produto.preco_venda, preco_venda_produto)
        self.assertTrue(produto.bloqueado)

    def test_edicao_produto_nao_bloqueado(self):
        id_produto = self.produto_valido.pk
        nova_descricao = 'Nova Descrição'
        novo_preco_venda = 100
        content = {
            'descricao': nova_descricao,
            'preco_venda': novo_preco_venda,
        }

        response = client.patch(
            f'/api/estoque/produtos/{id_produto}/',
            content,
            content_type='application/json',
        )

        produto = Produto.objects.get(pk=id_produto)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(produto.descricao, nova_descricao)
        self.assertEqual(produto.preco_venda, novo_preco_venda)
        self.assertFalse(produto.bloqueado)