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

    def test_cadastro_produto_preco_venda_negativo(self):
        descricao_produto = self.preco_venda_negativo.get('descricao')
        response = client.post(
            '/api/estoque/produtos/',
            self.preco_venda_negativo,
            content_type='application/json',
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(Produto.objects.filter(descricao=descricao_produto))
