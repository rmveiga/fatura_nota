def gera_numero_notafiscal(ultima_nota) -> int:
    if ultima_nota:
        ultimo_numero = ultima_nota.numero
        return ultimo_numero + 1
    return 1


def gera_numero_pedido(ultimo_pedido) -> int:
    if ultimo_pedido:
        ultimo_numero = ultimo_pedido.numero
        return ultimo_numero + 1
    return 1
