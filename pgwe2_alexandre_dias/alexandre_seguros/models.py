from django.db import models
# Create your models here.

## Tabela Cliente ##

class Cliente(models.Model):
   nome = models.CharField(max_length =45)
   sobrenome = models.CharField(max_length =45)
   rg = models.CharField(max_length =45)
   cpf = models.CharField(max_length =45)
   

class Cliente_has_carro(models.Model):    
    cliente_id = models.ManyToManyField(Cliente)
    carro_id = models.CharField(max_length =45)
    

class Carro(models.Model):
    marca = models.CharField(max_length =45)
    placa = models.CharField(max_length =45)
    ano = models.CharField(max_length =45)
    apolice_id = models.CharField(max_length =45)
    

class Apolice(models.Model):
    nome = models.CharField(max_length =45)
    preco = models.CharField(max_length =45)
    descricao = models.CharField(max_length =45)
    

class Accidente(models.Model):
    detalhe = models.CharField(max_length =45)
    data = models.DateField()
    carro_id = models.ForeignKey(Carro, on_delete=models.CASCADE)
    