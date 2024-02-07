#Exercicio81

class Livro:
    def __init__(self):
        print('A começar a criar livro...')
        self.__titulo = ''
        self.__ano = 0
        self.__autor = ''
        self.__disponibilidade = False

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def disponibilidade(self):
        if disponibilidade is True:
            return f'O livro está disponivel'
        else:
            return f'O livro não se encontra disponivel'

    @disponibilidade.setter
    def disponibilidade(self, disponibilidade):
        self.__disponibilidade = disponibilidade


print('----BIBLIOTECA----')
coisa = input('Clique ENTER para adicionar um novo livro...')
titulo = input('TITULO: ')
ano = int(input('ANO: '))
autor = input('AUTOR: ')
disponibilidade = input('DISPONIBILDIADE: ').strip().lower()
if disponibilidade == 's':
    disponibilidade = True
else:
    disponibilidade = False

novo_livro = Livro()
novo_livro.titulo = titulo
novo_livro.ano = ano
novo_livro.autor = autor

print(novo_livro.autor)
print(novo_livro.titulo)
print(novo_livro.ano)
print(novo_livro.disponibilidade)
