import re
from rest_framework.exceptions import ValidationError

CPFS_CONHECIDOS_INVALIDOS = [
    '00000000000',
    '11111111111',
    '22222222222',
    '33333333333',
    '44444444444',
    '55555555555',
    '66666666666',
    '77777777777',
    '88888888888',
    '99999999999',
]


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

    def cpf_valido(self, cpf_sem_mascara):
        if cpf_sem_mascara in CPFS_CONHECIDOS_INVALIDOS:
            return False
        if not self._primeiro_digito_cpf_valido(cpf_sem_mascara):
            return False
        if not self._segundo_digito_cpf_valido(cpf_sem_mascara):
            return False

        return True

    def cnpj_valido(self, cnpj_sem_mascara):
        if not self._primeiro_digito_cnpj_valido(cnpj_sem_mascara):
            return False
        if not self._segundo_digito_cnpj_valido(cnpj_sem_mascara):
            return False

        return True

    def valida_cpf_cnpj(self, cpf_cnpj):
        cpf_cnpj_temp = self.remove_mascara_de_numero(cpf_cnpj)

        if len(cpf_cnpj_temp) == 11:
            return self.cpf_valido(cpf_cnpj_temp)
        elif len(cpf_cnpj_temp) == 14:
            return self.cnpj_valido(cpf_cnpj_temp)
        else:
            return False

    def valida_cpf_cnpj_api(self, cpf_cnpj):
        if not self.valida_cpf_cnpj(cpf_cnpj):
            raise ValidationError(f'CPF/CNPJ Inválido: {cpf_cnpj}')

class Formatador:

    @staticmethod
    def numero_telefone(numero):
        if len(numero) == 8:
            return f'{numero[:4]}-{numero[4:]}'
        elif len(numero) == 9:
            return f'{numero[:5]}-{numero[5:]}'
        else:
            return numero

    @staticmethod
    def numero_telefone_completo(numero, cod_pais=None, ddd=None):
        resultado = ''

        if cod_pais:
            resultado += f'+{cod_pais} '
        if ddd:
            resultado += f'({ddd}) '
        if len(numero) == 8:
            resultado += f'{numero[:4]}-{numero[4:]}'
        elif len(numero) == 9:
            resultado += f'{numero[:5]}-{numero[5:]}'
        else:
            resultado += numero

        return resultado

    @staticmethod
    def cep(cep):
        return f'{cep[:5] - cep[5:]}'

    @staticmethod
    def cpf_cnpj(cpf_cnpj):
        if len(cpf_cnpj) == 11:
            return f'{cpf_cnpj[:3]}.{cpf_cnpj[3:6]}.{cpf_cnpj[6:9]}-{cpf_cnpj[9:]}'
        if len(cpf_cnpj) == 14:
            return f'{cpf_cnpj[:2]}.{cpf_cnpj[2:5]}.{cpf_cnpj[5:8]}/{cpf_cnpj[8:12]}-{cpf_cnpj[12:]}'


if __name__ == '__main__':
    pass
