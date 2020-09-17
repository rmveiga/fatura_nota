from django.test import TestCase, Client
from rest_framework import status

from datetime import datetime, timedelta

from estoque.models import Produto, MovimentoEstoque

client = Client()


class MovimentoEstoqueTest(TestCase):
    def setUp(self) -> None:
        self.data_atual = datetime.now().date()
        self.data_futura = datetime.now().date() + timedelta(1)

        self.produto_valido = Produto.objects.create(
            descricao='Produto Válido',
            preco_venda=1,
        )
        self.data_movimento_futuro = {
            'produto': self.produto_valido.pk,
            'data_movimento': self.data_futura,
            'tipo_movimento': 1,
            'quantidade': 1,
            'valor': 1,
        }

    def test_cadastro_data_movimento_futuro(self):
        id_produto = self.produto_valido.pk
        response = client.post(
            '/api/estoque/movimentos/',
            self.data_movimento_futuro,
            content_type='application/json',
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(MovimentoEstoque.objects.filter(
            produto__id=id_produto, data_registro=self.data_atual
        ))