#exercicio77

class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def depositar(self, value):
        self.saldo += value
        print(f'Você depositou {value} e a sua contou ficou com {self.saldo}')

    def levantar(self, value):
        if value > self.limite:
            print(f'O seu máximo de levantamento é {self.limite}')
        else:
            self.saldo -= value
            print(f'Você levantou {value} e a sua conta ficou com {self.saldo}')

    def ver_saldo(self):
        print(f'O saldo atual da sua conta é {self.saldo}')

conta1 = ContaBancaria('Tiago', 30000, 400)

print('-' * 30, 'MULTIBANCO', '-' * 30)
while True:
    print('[1] - Consultar Saldo')
    print('[2] - Levantar dinheiro')
    print('[3] - Depositar dinheiro')
    print('[4] - Sair')
    opcao = int(input('--> '))
    if opcao == 1:
        conta1.ver_saldo()
    elif opcao == 2:
        conta1.levantar(int(input('Que valor quer levantar?: ')))
    elif opcao == 3:
        conta1.depositar(int(input('Que valor quer depositar?: ')))
    elif opcao == 4:
        print('A sair do programa')
        break
    cont = input('Deseja continuar a usar o ATM? [S/N]: ').lower().strip()
    if cont == 'n':
        break


