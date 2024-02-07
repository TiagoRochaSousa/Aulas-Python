#Exercicio75

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostra(self):
        print(f'O livro {self.titulo} foi escrito pelo {self.autor}')

livro1 = Livro('Hobbit', 'Tolkien')

livro1.mostra()
