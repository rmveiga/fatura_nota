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