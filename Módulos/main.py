#importar a funcao
"""import functions --> aqui tem que levar functions.antes da funcao"""

from functions import soma

#programa principal
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

print(f'A soma entre {num1} e {num2} é igual a {soma(num1, num2)}')
