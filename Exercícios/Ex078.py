#Exercicio78

import math

class Circulo:
    def __init__(self, raio):
        self.__raio = raio

    def get_raio(self):
        return f'o valor do raio é {self.__raio}'

    def set_raio(self, valor):
        print(f'O valor do raio foi alterado para {valor}')
        self.__raio = valor

    def area(self):
        return f'A área do circulo é {math.pi * (self.__raio * self.__raio)}'

    def perimetro(self):
        return f'O perimetro do circulo é {2 * math.pi * self.__raio}'


circulo = Circulo(5)
print(circulo.get_raio())
print(circulo.area())
print(circulo.perimetro())


circulo.set_raio(10)
print(circulo.area())
print(circulo.perimetro())
