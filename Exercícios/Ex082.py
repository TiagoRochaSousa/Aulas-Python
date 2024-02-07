#Exercicio82

class Produto:
    def __init__(self, nome, stock):
        self._nome = nome
        self._stock = stock

    @property
    def stock(self):
        return 'Stock indisponivel' if self._stock == 0 and self._stock < 0 else f'{self._stock}'

    @stock.setter
    def stock(self, valor):
        self._stock = valor

    def mostrar_stock(self):
        return f'O stock está com {self._stock} produtos'

    def aumentar_stock(self, aumento):
        self._stock += aumento

produto = Produto('arroz', 1234)
print(produto.mostrar_stock())
print()
print()
produto.aumentar_stock(50)
print(produto.mostrar_stock())
