#Exercicio74

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

livro1 = Livro('The Hobbit', 'Tolkien')
livro2 = Livro('Senhor dos Aneis', 'Tolkien')
livro3 = Livro('Cujo', 'Stephen King')

print(f'O livro {livro1.titulo} tem o autor {livro1.autor}')
print(f'O livro {livro2.titulo} tem o autor {livro2.autor}')
print(f'O livro {livro3.titulo} tem o autor {livro3.autor}')
