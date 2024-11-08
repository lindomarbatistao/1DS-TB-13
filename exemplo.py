import sqlite3
import pandas as pd

class Ecommerce:
    def __init__ (self, db='db.sqlite3'):
        self.conn = sqlite3.connect(db)
        self.menu()

    def menu(self):
        while True:
            print('\n'
                '[1]-Create\n'
                '[2]-Read\n'
                '[3]-Update\n'
                '[4]-Delete\n'
                '[5]-Exit\n\n'
                )
            op = int(input('Escolha uma opção: '))
            match op:
                case 1:
                    self.menu_create()
                case 2:
                    self.read()
                case 3:
                    df = pd.read_sql_query('SELECT * FROM api_produto', self.conn)
                    print(df)
                    valor = int(input('ID: '))
                    query = f'SELECT * FROM api_produto WHERE id = {valor}'
                    df = pd.read_sql_query(query, self.conn)
                    print(df)
                case 4:
                    print('Delete')
                case 5:
                    break
                case _:
                    print('Opção inválida.')
    
    def create(self, titulo, preco, descricao, imagemProduto,
               categoriaProduto, classProduto, exibirHome):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO api_produto (tituloProduto, preco, descricao, imagemProduto,
               categoriaProduto, classProduto, exibirHome)
            VALUES(?,?,?,?,?,?,?)""",
                (titulo, preco, descricao, imagemProduto,
               categoriaProduto, classProduto, exibirHome))
        self.conn.commit()
        print('Produto cadastrado com sucesso!!!')
    
    def menu_create(self):
        print(
            '\n'
            '[1]-Título\n'
            '[2]-Preço\n'
            '[3]-Descrição\n'
            '[4]-Imagem\n'
            '[5]-Categoria\n'
            '[6]-Classificação\n'
            '[7]-Exibir\n'
        )
        titulo = input("Título: ")
        preco = float(input('Preço: '))
        descricao = input("Descrição: ")
        imagemProduto = input("Imagem: ")
        categoriaProduto = input("Categoria: ")
        classProduto = input("Classificação: ")
        exibirHome = input("Exibir(True, False): ")
        self.create(titulo, preco, descricao, imagemProduto,
               categoriaProduto, classProduto, exibirHome)

    def read(self):
        print('\n'
              '[1]-Listar todos os produtos\n'
              '[2]-Listar por ID'
              )
        op = int(input("Escolha a opção: "))
        match op:
            case 1:
                df = pd.read_sql_query('SELECT * FROM api_produto', self.conn)
                return print(df)
            case 2:
                valor = int(input('ID: '))
                query = f'SELECT * FROM api_produto WHERE id = {valor}'
                df = pd.read_sql_query(query, self.conn)
                return print(df)
            case _:
                print("Escolha uma opção válida...")

    def update(self, id, titulo=None, preco=None, descricao=None, imagemProduto=None,
               categoriaProduto=None, classProduto=None, exibirHome=None):
        cursor = self.conn.cursor()
        campos = []
        valores = []

        if titulo:
            campos.append('tituloProduto = ?')   
            valores.append(titulo) 
        if preco:
            campos.append('preco = ?')   
            valores.append(preco) 
        if descricao:
            campos.append('descricao = ?')   
            valores.append(descricao) 
        if imagemProduto:
            campos.append('imagemProduto = ?')   
            valores.append(imagemProduto) 
        if categoriaProduto:
            campos.append('categoriaProduto = ?')   
            valores.append(categoriaProduto) 
        if classProduto:
            campos.append('classProduto = ?')   
            valores.append(classProduto) 
        if exibirHome is not None:
            campos.append('exibirHome = ?')   
            valores.append(exibirHome) 

        if campos:
            valores.append(id)
            cursor.execute(f'''
                UPDATE api_produto SET {', '.join(campos)} WHERE id = ?
                ''', valores)
            self.conn.commit()
            print('Produto atualizado com sucesso...')
        else:
            print('Nenhum produto atualizado...')



ecommerce = Ecommerce()