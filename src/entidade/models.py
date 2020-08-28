from django.db import models

from entidade.util import Formatador, Validador


validador = Validador()


class Entidade(models.Model):
    data_cadastro = models.DateField(auto_now_add=True, verbose_name='Data de Cadastro')
    nome = models.CharField(max_length=150, verbose_name='Nome')
    cpf_cnpj = models.CharField(
        max_length=14, validators=[validador.valida_cpf_cnpj_api], verbose_name='CPF/CNPJ'
    )
    observacao = models.TextField(null=True, blank=True, verbose_name='Observação')
    cliente = models.BooleanField(verbose_name='Cliente')
    fornecedor = models.BooleanField(verbose_name='Fornecedor')

    class Meta:
        db_table = 'entidade'

    def __str__(self):
        return self.nome


class TipoTelefone(models.Model):
    descricao = models.CharField(max_length=50, verbose_name='Descrição')

    class Meta:
        db_table = 'tipo_telefone'

    def __str__(self):
        return self.descricao


class Telefone(models.Model):
    entidade = models.ForeignKey(Entidade, on_delete=models.CASCADE, verbose_name='Entidade')
    tipo_telefone = models.ForeignKey(
        TipoTelefone, on_delete=models.CASCADE, verbose_name='Tipo de Telefone'
    )
    codigo_pais = models.CharField(max_length=3, verbose_name='Código do País')
    ddd = models.CharField(max_length=2, verbose_name='DDD')
    numero = models.CharField(max_length=9, verbose_name='Número')
    ramal = models.CharField(max_length=5, verbose_name='Ramal')

    class Meta:
        db_table = 'telefone'

    def __str__(self):
        return f'{Formatador.numero_telefone(self.numero, cod_pais=self.codigo_pais, ddd=self.ddd)}'


class TipoEndereco(models.Model):
    descricao = models.CharField(max_length=50, verbose_name='Descrição')

    class Meta:
        db_table = 'tipo_endereco'

    def __str__(self):
        return self.descricao


class Endereco(models.Model):
    entidade = models.ForeignKey(Entidade, on_delete=models.CASCADE, verbose_name='Entidade')
    tipo_endereco = models.ForeignKey(
        TipoEndereco, on_delete=models.CASCADE, verbose_name='Tipo de Endereço'
    )
    cep = models.CharField(max_length=8, verbose_name='CEP')
    logradouro = models.CharField(max_length=150, verbose_name='Logradouro')
    numero = models.CharField(max_length=10, verbose_name='Número')
    complemento = models.CharField(max_length=50, verbose_name='Complemento')
    cidade = models.CharField(max_length=50, verbose_name='Cidade')
    estado = models.CharField(max_length=50, verbose_name='Estado')
    uf = models.CharField(max_length=2, verbose_name='UF')
    pais = models.CharField(max_length=25, verbose_name='País')
    observacao = models.TextField(verbose_name='Observação')

    class Meta:
        db_table = 'endereco'

    def __str__(self):
        return self.logradouro
