#ProjetoGrupo001

#Definir lista dos livros

biblioteca = list()

#DEfinir dicionarios


#Adicionar livros
while True:
    livros = dict()
    '''    #Input do titulo
    if len(biblioteca) > 0:
        titulo = input("Digite o título do livro: ").strip().lower()
        if titulo not in livros["Titulo"]:
            livros["Titulo"] = titulo
        else:
            titulo = input("Esse livro já existe na biblioteca insira outro livro: ").strip().lower()
    else:
        livros["Titulo"] = input("Digite o título do livro: ").strip().lower()'''

    #Input de varios autores
    lista_autores = list()
    while True:
        autores = [input("Digite o autor do livro: ")]
        lista_autores.append(autores)
        continuar = input("O livro tem mais autores?: [S/N] ").strip().lower()
        if continuar == "n":
            break

    livros["Autores"] = lista_autores

    #input do ISBN
    isbn = input("Digite o ISBN do livro: ")
    while len(isbn) != 13 or isbn.isnumeric() is False:
        isbn = input("Digite corretamente o ISBN do livro: ")
    else:
        livros["ISBN"] = isbn

    #input do Ano de Publicação
    ano_publicacao = input("Digite o ano de publicação do livro: ")
    while len(ano_publicacao) != 4 or ano_publicacao.isnumeric() is False:
        ano_publicacao = input("Digite o ano de publicação do livro: ")
    else:
        livros["Ano de publicação"] = ano_publicacao

    #input editora
    livros["Editora"] = input("Digite o nome da editora do livro:").strip()

    #input de generos
    categorias = list()
    while True:
        cat = [input("Digite a categoria/género do livro: ")]
        categorias.append(cat)
        continuar = input("O livro pode ser identificado com outra categoria?: [S/N] ").strip().lower()
        if continuar == "n":
            break

    livros["Categorias"] = categorias

    #input de status de disponibilidade
    status = "Dísponivel"
    livros["Status"] = status

    #Término
    terminar = input("Deseja registar mais algum livro? [S/N]: ").strip().upper()
    if terminar == "N":
        break

    biblioteca.append(livros)

print(biblioteca)
