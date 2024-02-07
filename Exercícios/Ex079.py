#Exercicio79

class ContaBancaria:
    def __init__(self):
        self.__nib = 'NIB'
        self.__titular = 'TITULAR'
        self.__saldo = 0
        self.__limite = 0

    def get_nib(self):
        return self.__nib

    def set_nib(self, nib):
        self.__nib = nib

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


print('Crie a sua conta bancária')
print()

titular = input('Digite o titular da conta: ')
nib = input('Digite o nib da conta: ')
saldo = input('Digite o saldo da conta: ')
limite = input('Digite o limite da conta: ')

conta = ContaBancaria()
conta.set_titular(titular)
conta.set_nib(nib)
conta.set_saldo(saldo)
conta.set_limite(limite)
print()
print(f'Titular da conta : {conta.get_titular()}')
print(f'NIB da conta: {conta.get_nib()}')
print(f'Saldo da conta: {conta.get_saldo()}')
print(f'Limite da conta: {conta.get_limite()}')
