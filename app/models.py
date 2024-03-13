from django.db import models

# Create your models here.

class UF(models.Model):

    nome = models.CharField(max_length=2)

    class Meta:
        
        verbose_name_plural = 'UFs'

    def __str__(self):

        return self.nome

class Cidade(models.Model):

    nome = models.CharField(max_length=100)
    uf = models.ForeignKey(UF, on_delete = models.CASCADE)

    class Meta:

        verbose_name_plural = "Cidades"

    def __str__(self):

        return f'{self.nome} - {self.uf}'
    
class Bairro(models.Model):

    nome = models.CharField(max_length=50)

    class Meta:
        
        verbose_name_plural = 'Bairros'

    def __str__(self):

        return self.nome
    
class TipoLogradouro(models.Model):

    nome = models.CharField(max_length=100)

    class Meta:

        verbose_name_plural = "Tipos de Logradouros"

    def __str__(self):

        return self.nome
    
class TipoImovel(models.Model):

    nome = models.CharField(max_length=100)

    class Meta:

        verbose_name_plural = "Tipos de Imóveis"

    def __str__(self):

        return self.nome
    
class Cargo(models.Model):

    nome = models.CharField(max_length=100)

    class Meta:

        verbose_name_plural = "Cargos"

    def __str__(self):

        return self.nome

class Pessoa(models.Model):

    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15)
    rg = models.CharField(max_length=20)
    data_nasc = models.DateField()
    email = models.CharField(max_length=80)
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE)

    class Meta:

        verbose_name_plural = "Pessoas"

    def __str__(self):

        return self.nome
    
class Logradouro(models.Model):

    tipo = models.ForeignKey(TipoLogradouro, on_delete = models.CASCADE)
    nome = models.CharField(max_length=100)
    numero = models.PositiveIntegerField()
    complemento = models.CharField(max_length=100)
    bairro = models.ForeignKey(Bairro, on_delete = models.CASCADE)
    cep = models.CharField(max_length=20)

    class Meta:

        verbose_name_plural = "Logradouros"

    def __str__(self):

        return f'{self.tipo}, {self.nome}, {self.numero}'
    
class EstadoImovel(models.Model):

    estado = models.CharField(max_length=40)

    class Meta:

        verbose_name_plural = "Estados dos Imóveis"

    def __str__(self):

        return f'{self.estado}'
    
class RankingImovel(models.Model):

    nivel = models.PositiveIntegerField()

    class Meta:

        verbose_name_plural = "Rankings"

    def __str__(self):

        return f'{self.nivel}'

class Imovel(models.Model):

    nome = models.CharField(max_length=100)
    tipo_imovel = models.ForeignKey(TipoImovel, on_delete = models.CASCADE)
    descricao = models.CharField(max_length=500)
    area_construida = models.CharField(max_length=50)
    n_comodos = models.PositiveIntegerField()
    cor = models.CharField(max_length=40)
    n_vagas = models.PositiveIntegerField()
    tipo_logradouro = models.ForeignKey(TipoLogradouro, on_delete = models.CASCADE)
    logradouro = models.ForeignKey(Logradouro, on_delete = models.CASCADE)
    bairro = models.ForeignKey(Bairro, on_delete = models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE)
    uf = models.ForeignKey(UF, on_delete = models.CASCADE)
    cep = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.ForeignKey(EstadoImovel, on_delete = models.CASCADE)
    nivel = models.ForeignKey(RankingImovel, on_delete = models.CASCADE)

    class Meta:

        verbose_name_plural = "Imóveis"

    def __str__(self):

        return f'{self.tipo_imovel} - {self.nome}'
    
class Locatario(Pessoa):

    class Meta:

        verbose_name_plural = "Locatários"

    def __str__(self):

        return f'{self.nome}'
    
class Comprador(Pessoa):

    class Meta:

        verbose_name_plural = "Compradores"

    def __str__(self):

        return f'{self.nome}'
    
class FormaPagamento(models.Model):

    nome = models.CharField(max_length=50)

    class Meta:

        verbose_name_plural = "Formas de Pagamento"

    def __str__(self):

        return f'{self.nome}'

class Venda(models.Model):

    comprador = models.ForeignKey(Comprador, on_delete = models.CASCADE)
    imovel = models.ForeignKey(Imovel, on_delete = models.CASCADE)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete = models.CASCADE)

    class Meta:

        verbose_name_plural = "Vendas"

    def __str__(self):

        return f'{self.comprador} {self.imovel} {self.valor_venda}'

class Locacao(models.Model):

    locatario = models.ForeignKey(Locatario, on_delete = models.CASCADE)
    imovel = models.ForeignKey(Imovel, on_delete = models.CASCADE)
    valor_aluguel = models.DecimalField(max_digits = 10, decimal_places = 2)
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete = models.CASCADE)

    class Meta:

        verbose_name_plural = "Locações"

    def __str__(self):

        return f'{self.comprador} {self.imovel} {self.valor_aluguel}'
    