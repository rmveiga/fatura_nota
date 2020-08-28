import re

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


class Validacoes:

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

    def remove_mascara_de_numero(self, numero):
        return re.sub('[^0-9]', '', numero)

    def cpf_valido(self, cpf):
        cpf_temp = self.remove_mascara_de_numero(cpf)

        if len(cpf_temp) != 11:
            return False
        if cpf_temp in CPFS_CONHECIDOS_INVALIDOS:
            return False
        if not self._primeiro_digito_cpf_valido(cpf_temp):
            return False
        if not self._segundo_digito_cpf_valido(cpf_temp):
            return False

        return True


class Formatos:

    @staticmethod
    def numero_telefone(numero, cod_pais=None, ddd=None):
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
        return f'{cep[:5]-cep[5:]}'

    @staticmethod
    def cpf_cnpj(cpf_cnpj):
        if len(cpf_cnpj) == 11:
            return f'{cpf_cnpj[:3]}.{cpf_cnpj[3:6]}.{cpf_cnpj[6:9]}-{cpf_cnpj[9:]}'
        if len(cpf_cnpj) == 14:
            return f'{cpf_cnpj[:2]}.{cpf_cnpj[2:5]}.{cpf_cnpj[5:8]}/{cpf_cnpj[8:12]}-{cpf_cnpj[12:]}'


if __name__ == '__main__':
    cpf = '52998224725'
    v = Validacoes()
    if v.cpf_valido(cpf):
        print('VÁLIDO')
    else:
        print('INVÁLIDO')
