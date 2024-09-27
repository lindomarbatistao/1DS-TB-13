from django.db import models

class Produto(models.Model):
    codigoProduto = models.IntegerField(max_length=10)
    tituloProduto = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(max_length=500) 
    imagemProduto = models.CharField(max_length=255)
    categoriaProduto = models.CharField(max_length=255)
    classProduto = models.CharField(max_length=255)
    exibirHome = models.BooleanField(default=True)

