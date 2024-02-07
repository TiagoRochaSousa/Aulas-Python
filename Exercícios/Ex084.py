#Exercicio84

class Temperatura:
    def __init__(self, temperatura):
        self._temperatura = temperatura

    @property
    def temperatura(self):
        return f'{self._temperatura} Celsius'

    @temperatura.setter
    def temperatura(self, nova_temp):
        self._temperatura = nova_temp

    def converter_faren(self, temp):
        self._temperatura = (temp * (9/5)) + 32

    def converter_kelvin(self, temp):
        self._temperatura = temp + 273.15


