def divisao(a, b):
    div = a / b
    return div


try:
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    print(divisao(num1, num2))

except ZeroDivisionError:
    print(f'ERRO! A DIVISÃO POR ZERO NÃO É POSSIVEL')

except ValueError:
    print('O utilizador não digitou os números')

except EOFError:
    print('Erro do fabio')

except KeyboardInterrupt:
    print('\nO programa foi fechado inesperadamente')

else:
    print('A divisao é poossivel')

finally:
    print('TERMINOU')


