#Exercicio80

class Aluno:
    def __init__(self):
        self.__nome = 'Nome'
        self.__nota = 0
        self.__media = 0
        self.__situacao = 'status'

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_nota(self):
        return self.__nota

    def set_nota(self, nota):
        self.__nota = nota

    def media(self, media):
        pass



