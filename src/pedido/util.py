class Ferramentas:

    @staticmethod
    def gera_numero_pedido(ultimo_pedido) -> int:
        if ultimo_pedido:
            ultimo_numero = ultimo_pedido.numero
            return ultimo_numero + 1
        return 1
