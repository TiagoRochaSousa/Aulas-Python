"""#criar uma conta bancaria
#identidade, titular, saldo, limite
#levantar dinheiro, depositar dinheiro, extrato

def levantar_dinheiro(valor):
    if valor > conta['limite']:
        print('O seu valor limite é de 400')
    else:
        if conta['saldo'] > valor:
            conta['saldo'] -= valor


def depositar_dinheiro(valor):
        conta['saldo'] += valor

def extrato():
    print(f'A conta {conta['identidade']} tem o saldo de {conta['saldo']}€')

contas = list()

conta = {'identidade': input('ID: '),
         'titular': input('Nome: '),
         'saldo': int(input('Saldo: ')),
         'limite': int(input('Limite: '))}

print('Extrato')
extrato()
print('Deposito de 1000')
depositar_dinheiro(1000)
print('Extrato')
extrato()
print('Levanta 1000, tem de dar erro')
levantar_dinheiro(1000)
print('Extrato')
extrato()
print('Levanta 400, tem de dar')
levantar_dinheiro(400)
print('Extrato')
extrato()
"""

"""class Jogo:
    def __init__(self, titulo, consola, preco):
        self.titulo = titulo
        self.consola = consola
        self.preco = preco

jogo = Jogo('Palworld', 'PC', 29.90)

print(jogo.titulo)
print(jogo.consola)
print(jogo.preco)
"""

"""class Conta:
    def __init__(self, identidade, titular, saldo, limite):
        self.__identidade = identidade
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def levantar(self, valor):
        if valor > self.__limite:
            print('O seu limite é de 400€ diários.')
        else:
            if self.__saldo > valor:
                self.__saldo -= valor

    def depositar(self, valor):
        self.__saldo += valor

    def extrato(self):
        print(f'O valor da conta {self.__identidade} tem {self.__saldo}€ disponiveis')"""


"""class Conta:
    def __init__(self, nib, titular, saldo, limite):
        self.nib = nib
        self.titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, valor):
        self.__limite = valor"""


class Conta:
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def saldo(self):
        return f'O saldo da conta é: {self.__saldo}€'

    @saldo.setter
    def saldo(self, valor):
        if valor > 1000:
            print('Valor não autorizado')
        else:
            self.__saldo = valor
            print('Saldo modificado com sucesso')


conta = Conta('Ricardo', 1250, 400)
print(conta.saldo)
conta.saldo = int(input('Digite o novo saldo: '))
print(conta.saldo)
