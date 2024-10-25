import sqlite3

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
                    self.create()
                case 2:
                    print('Read')
                case 3:
                    print('Update')
                case 4:
                    print('Delete')
                case 5:
                    break
                case _:
                    print('Opção inválida.')
    
    def create(self, tituloProduto, preco, descricao, imagemProduto,
               categoriaProduto, classProduto, exibirHome):
        cursor = self.conn.cursor()
        


ecommerce = Ecommerce()