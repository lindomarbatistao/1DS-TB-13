from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fiels = [
           'id',
           'codigoProduto',
           'tituloProduto',
           'preco',
           'descricao',
           'imagemProduto',
           'categoriaProduto',
           'classProduto',
           'exibirHome'
        ]


    