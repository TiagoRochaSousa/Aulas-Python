#Exercicio76

class Produto:
    def __init__(self, nome, stock):
        self.nome = nome
        self.stock = stock

    def quantidade(self):
        print(f'O produto {self.nome} tem {self.stock} unidades em stock')

    def aumento_stock(self, valor):
        self.stock += valor


produto1 = Produto('xbox', 5)
produto1.quantidade()
print('Vou acrescentar ao stock')
produto1.aumento_stock(20)
produto1.quantidade()
