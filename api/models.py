from django.db import models

class Produto(models.Model):
    codigoProduto = models.IntegerField(max_length=10)
    tituloProduto = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(max_length=500)    
# 	descricao (str): Descrição detalhada do produto.
# 	imagemProduto (str): Caminho ou URL da imagem do produto.
# 	categoriaProduto (str): Categoria à qual o produto pertence.
# 	classificacaoProduto (float): Classificação média do produto com base nas avaliações dos usuários.
# 	exibirHome (bool): Indica se o produto deve ser exibido na página inicial.
