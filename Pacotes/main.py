import header
import matematica

"""ou
from header import header
from matematica import calculadora
"""


header.header('Calculador Mágica')
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
sinal = input('Qual operação deseja fazer? [+ - x /]: ')

print(f'{num1} {sinal} {num2} = {matematica.calculadora(num1, num2, sinal)}')
