import re
from random import randint
from rest_framework.exceptions import ValidationError

from . import constantes


class Validador:
    mensagens_validacao = constantes.MENSAGENS.get('validação')

    def _primeiro_digito_cpf_valido(self, cpf_sem_mascara):
        digito_gerado = self._gera_primeiro_digito_cpf(cpf_sem_mascara[:9])
        primeiro_digito = cpf_sem_mascara[-2]

        return digito_gerado == primeiro_digito

    def _segundo_digito_cpf_valido(self, cpf_sem_mascara):
        digito_gerado = self._gera_segundo_digito_cpf(cpf_sem_mascara[:10])
        segundo_digito = cpf_sem_mascara[-1]

        return digito_gerado == segundo_digito

    def _primeiro_digito_cnpj_valido(self, cnpj_sem_mascara):
        resultado = 0
        sequencia_1 = list(range(2, 6))
        sequencia_2 = list(range(2, 10))
        primeiro_digito = cnpj_sem_mascara[-2]
        for i in cnpj_sem_mascara[:12]:
            if sequencia_1:
                resultado += int(i) * sequencia_1[-1]
                sequencia_1.pop()
            else:
                resultado += int(i) * sequencia_2[-1]
                sequencia_2.pop()

        resto = resultado % 11
        if resto < 2:
            resto = 0
        else:
            resto = 11 - resto

        return str(resto) == primeiro_digito

    def _segundo_digito_cnpj_valido(self, cnpj_sem_mascara):
        resultado = 0
        sequencia_1 = list(range(2, 7))
        sequencia_2 = list(range(2, 10))
        segundo_digito = cnpj_sem_mascara[-1]
        for i in cnpj_sem_mascara[:13]:
            if sequencia_1:
                resultado += int(i) * sequencia_1[-1]
                sequencia_1.pop()
            else:
                resultado += int(i) * sequencia_2[-1]
                sequencia_2.pop()

        resto = resultado % 11
        if resto < 2:
            resto = 0
        else:
            resto = 11 - resto

        return str(resto) == segundo_digito

    def _gera_corpo_cpf(self):
        corpo_cpf = str()
        for i in range(9):
            corpo_cpf += str(randint(1, 9))
        return corpo_cpf

    def _gera_primeiro_digito_cpf(self, corpo_cpf):
        resultado = 0
        numeros = list(range(2, 11))
        for i in corpo_cpf:
            resultado += int(i) * numeros[-1]
            numeros.pop()

        resto = (resultado * 10) % 11
        if resto == 10:
            resto = 0

        return str(resto)

    def _gera_segundo_digito_cpf(self, corpo_cpf):
        resultado = 0
        numeros = list(range(2, 12))
        for i in corpo_cpf:
            resultado += int(i) * numeros[-1]
            numeros.pop()

        resto = (resultado * 10) % 11
        if resto == 10:
            resto = 0

        return str(resto)

    def gerador_cpf(self):
        cpf = self._gera_corpo_cpf()
        cpf += self._gera_primeiro_digito_cpf(cpf)
        cpf += self._gera_segundo_digito_cpf(cpf)
        return cpf

    def remove_mascara_de_numero(self, numero):
        return re.sub('[^0-9]', '', numero)

    def verifica_cpf(self, cpf_sem_mascara):
        if cpf_sem_mascara in constantes.CPFS_CONHECIDOS_INVALIDOS:
            return False
        if not self._primeiro_digito_cpf_valido(cpf_sem_mascara):
            return False
        if not self._segundo_digito_cpf_valido(cpf_sem_mascara):
            return False
        return True

    def verifica_cnpj(self, cnpj_sem_mascara):
        if not self._primeiro_digito_cnpj_valido(cnpj_sem_mascara):
            return False
        if not self._segundo_digito_cnpj_valido(cnpj_sem_mascara):
            return False
        return True

    def verifica_cpf_cnpj(self, cpf_cnpj):
        cpf_cnpj_temp = self.remove_mascara_de_numero(cpf_cnpj)

        if len(cpf_cnpj_temp) == 11:
            return self.verifica_cpf(cpf_cnpj_temp)
        elif len(cpf_cnpj_temp) == 14:
            return self.verifica_cnpj(cpf_cnpj_temp)
        else:
            return False

    def valida_cpf_cnpj(self, cpf_cnpj):
        if not self.verifica_cpf_cnpj(cpf_cnpj):
            mensagem_cpf_cnpj = self.mensagens_validacao.get('entidade').get('cpf_cnpj')
            raise ValidationError(mensagem_cpf_cnpj(cpf_cnpj))

    def verifica_ddd(self, ddd, codigo_pais):
        if int(codigo_pais) == constantes.CODIGO_TELEFONICO_BRASIL:
            if int(ddd) not in constantes.CODIGOS_AREA_BRASIL.keys():
                return False
            return True

    def valida_ddd(self, ddd, codigo_pais):
        if not self.verifica_ddd(ddd, codigo_pais):
            mensagem_ddd = self.mensagens_validacao.get('telefone').get('ddd')
            raise ValidationError(mensagem_ddd(ddd))

    def verifica_tamanho_numero_telefone(self, numero, codigo_pais):
        numero_temp = self.remove_mascara_de_numero(numero)
        if int(codigo_pais) == constantes.CODIGO_TELEFONICO_BRASIL:
            if len(numero_temp) < 8:
                return False
            return True

    def valida_tamanho_numero_telefone(self, numero, codigo_pais):
        if not self.verifica_tamanho_numero_telefone(numero, codigo_pais):
            mensagem_numero_telefone = self.mensagens_validacao.get('telefone').get('numero')
            raise ValidationError(mensagem_numero_telefone(numero))

    def verifica_se_numero_negativo(self, numero):
        if numero < 0:
            return True
        return False

    def valida_preco_venda_produto_api(self, preco_venda):
        if self.verifica_se_numero_negativo(preco_venda):
            mensagem_preco_venda = self.mensagens_validacao.get('produto').get('preco_venda')
            raise ValidationError(mensagem_preco_venda(preco_venda))

    def valida_quantidade_produto_api(self, quantidade):
        if self.verifica_se_numero_negativo(quantidade):
            mensagem_quantidade = self.mensagens_validacao.get('produto').get('quantidade')
            raise ValidationError(mensagem_quantidade(quantidade))
