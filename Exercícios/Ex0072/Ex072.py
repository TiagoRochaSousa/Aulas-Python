import header
import funciones

header.header('Programa Matematico')

def menu():
    print('----Escolha uma opção----')
    print('1 - [SOMA]')
    print('2 -[SUBTRAÇÃO]')
    print('3 - [MULTIPLICAÇÃO]')
    print('4 - [DIVISÃO]')
    print('5 - [TABUADA]')
    print('6 - [PAR/ÍMPAR]')
    print('7 - [PRIMO]')
    print('8 - [FACTORIAL]')


while True:
    menu()
    escolha = int(input('--->'))
    try:
        if escolha == 1:
            num1 = int(input('Digite o primeiro numero: '))
            num2 = int(input('Digite o segundo numero: '))
            print(funciones.soma(num1, num2))
        elif escolha == 2:
            num1 = int(input('Digite o primeiro numero: '))
            num2 = int(input('Digite o segundo numero: '))
            print(funciones.subtrai(num1, num2))
        elif escolha == 3:
            num1 = int(input('Digite o primeiro numero: '))
            num2 = int(input('Digite o segundo numero: '))
            print(funciones.multiplica(num1, num2))
        elif escolha == 4:
            num1 = int(input('Digite o primeiro numero: '))
            num2 = int(input('Digite o segundo numero: '))
            print(funciones.divide(num1, num2))
        elif escolha == 5:
            num = int(input('Digite o numero para recerber a sua tabuada: '))
            print(funciones.tabuada(num))
            opcao = input('Deseja prosseguir com o programa? [S/N]: ')
            if opcao == 'N':
                print('O programa vai encerrar')
                break
    except ValueError:
        print('coise')
