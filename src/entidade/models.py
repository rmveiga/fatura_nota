from django.db import models

from utilitario import validadores, formatadores

validador = validadores.Validador()


class Entidade(models.Model):
    data_cadastro = models.DateField(auto_now_add=True, verbose_name='Data de Cadastro')
    nome = models.CharField(max_length=150, verbose_name='Nome')
    cpf_cnpj = models.CharField(
        max_length=14, validators=[validador.valida_cpf_cnpj], verbose_name='CPF/CNPJ', name='cpf_cnpj'
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
        TipoTelefone, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Tipo de Telefone'
    )
    codigo_pais = models.CharField(max_length=3, verbose_name='Código do País')
    _ddd = models.CharField(max_length=2, verbose_name='DDD', name='ddd')
    _numero = models.CharField(max_length=9, verbose_name='Número', name='numero')
    ramal = models.CharField(max_length=5, blank=True, verbose_name='Ramal')

    class Meta:
        db_table = 'telefone'

    def __str__(self):
        return formatadores.numero_telefone_completo(self.numero, cod_pais=self.codigo_pais, ddd=self.ddd)

    @property
    def ddd(self):
        return self._ddd

    @ddd.setter
    def ddd(self, value):
        validador.valida_ddd(value, self.codigo_pais)
        self._ddd = value

    @property
    def numero(self):
        return formatadores.numero_telefone(self._numero)

    @numero.setter
    def numero(self, value):
        validador.valida_tamanho_numero_telefone(value, self.codigo_pais)
        self._numero = validador.remove_mascara_de_numero(value)


class TipoEndereco(models.Model):
    descricao = models.CharField(max_length=50, verbose_name='Descrição')

    class Meta:
        db_table = 'tipo_endereco'

    def __str__(self):
        return self.descricao


class Endereco(models.Model):
    entidade = models.ForeignKey(Entidade, on_delete=models.CASCADE, verbose_name='Entidade')
    tipo_endereco = models.ForeignKey(
        TipoEndereco, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Tipo de Endereço'
    )
    _cep = models.CharField(max_length=8, verbose_name='CEP', name='cep')
    logradouro = models.CharField(max_length=150, verbose_name='Logradouro')
    numero = models.CharField(max_length=10, verbose_name='Número')
    complemento = models.CharField(max_length=50, blank=True, verbose_name='Complemento')
    cidade = models.CharField(max_length=50, verbose_name='Cidade')
    estado = models.CharField(max_length=50, verbose_name='Estado')
    uf = models.CharField(max_length=2, verbose_name='UF')
    pais = models.CharField(max_length=25, verbose_name='País')
    observacao = models.TextField(blank=True, verbose_name='Observação')

    class Meta:
        db_table = 'endereco'

    def __str__(self):
        return self.logradouro

    @property
    def cep(self):
        return formatadores.cep(self._cep)

    @cep.setter
    def cep(self, value):
        self._cep = validador.remove_mascara_de_numero(value)
