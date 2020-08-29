import re
from rest_framework.exceptions import ValidationError

from . import constantes


class Validador:

    def _primeiro_digito_cpf_valido(self, cpf_sem_mascara):
        resultado = 0
        numeros = list(range(2, 11))
        primeiro_digito = cpf_sem_mascara[-2]
        for i in cpf_sem_mascara[:9]:
            resultado += int(i) * numeros[-1]
            numeros.pop()

        resto = (resultado * 10) % 11
        if resto == 10:
            resto = 0

        return str(resto) == primeiro_digito

    def _segundo_digito_cpf_valido(self, cpf_sem_mascara):
        resultado = 0
        numeros = list(range(2, 12))
        segundo_digito = cpf_sem_mascara[-1]
        for i in cpf_sem_mascara[:10]:
            resultado += int(i) * numeros[-1]
            numeros.pop()

        resto = (resultado * 10) % 11
        if resto == 10:
            resto = 0

        return str(resto) == segundo_digito

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

    def remove_mascara_de_numero(self, numero):
        return re.sub('[^0-9]', '', numero)

    def valida_cpf(self, cpf_sem_mascara):
        if cpf_sem_mascara in constantes.CPFS_CONHECIDOS_INVALIDOS:
            return False
        if not self._primeiro_digito_cpf_valido(cpf_sem_mascara):
            return False
        if not self._segundo_digito_cpf_valido(cpf_sem_mascara):
            return False
        return True

    def valida_cnpj(self, cnpj_sem_mascara):
        if not self._primeiro_digito_cnpj_valido(cnpj_sem_mascara):
            return False
        if not self._segundo_digito_cnpj_valido(cnpj_sem_mascara):
            return False
        return True

    def valida_cpf_cnpj(self, cpf_cnpj):
        cpf_cnpj_temp = self.remove_mascara_de_numero(cpf_cnpj)

        if len(cpf_cnpj_temp) == 11:
            return self.valida_cpf(cpf_cnpj_temp)
        elif len(cpf_cnpj_temp) == 14:
            return self.valida_cnpj(cpf_cnpj_temp)
        else:
            return False

    def valida_cpf_cnpj_api(self, cpf_cnpj):
        if not self.valida_cpf_cnpj(cpf_cnpj):
            raise ValidationError(f'CPF/CNPJ Inválido: {cpf_cnpj}')

    def valida_ddd(self, ddd, codigo_pais):
        if int(codigo_pais) == constantes.CODIGO_TELEFONICO_BRASIL:
            if int(ddd) not in constantes.CODIGOS_AREA_BRASIL.keys():
                return False
            return True

    def valida_ddd_api(self, ddd, codigo_pais):
        if not self.valida_ddd(ddd, codigo_pais):
            raise ValidationError(f'DDD Inválido: {ddd}')