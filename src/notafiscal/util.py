class Ferramentas:

    @staticmethod
    def gera_numero_notafiscal(ultima_nota) -> int:
        if ultima_nota:
            ultimo_numero = ultima_nota.numero
            return ultimo_numero + 1
        return 1
