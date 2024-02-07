#exercicio83

class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    @property
    def titular(self):
        return f'Titular: {self._titular}'

    @titular.setter
    def titular(self, nome):
        self._titular = nome

    @property
    def saldo(self):
        return f'Saldo: {self._saldo}'

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    @property
    def limite(self):
        return f'Limite: {self._limite}'

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    def depositar(self, value):
        self._saldo += value
        print(f'Você depositou {value} e a sua contou ficou com {self._saldo}')

    def levantar(self, value):
        if value > self._limite:
            print(f'O seu máximo de levantamento é {self._limite}')
        else:
            self._saldo -= value
            print(f'Você levantou {value} e a sua conta ficou com {self._saldo}')

    def ver_saldo(self):
        print(f'O saldo atual da sua conta é {self._saldo}')

conta = ContaBancaria('Tiago', 1235, 123)
conta.ver_saldo()
conta.depositar(500)
conta.ver_saldo()
conta.levantar(500)
conta.levantar(122)
conta.ver_saldo()
