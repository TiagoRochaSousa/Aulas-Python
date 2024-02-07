from time import sleep
from colorama import init, Fore, Style
from datetime import date
import openpyxl


# Initialize colorama
init(autoreset=True)


def menu_principal():
    menu_word = "=== Menu ==="
    print("\n" + Fore.CYAN + Style.BRIGHT + menu_word)
    print(Fore.YELLOW + "[1] Inserir Livros")
    print(Fore.YELLOW + "[2] Listar Livros")
    print(Fore.YELLOW + "[3] Pesquisar Livros")
    print(Fore.YELLOW + "[4] Remover Livros")
    print(Fore.YELLOW + "[5] Emprestar Livros")
    print(Fore.YELLOW + "[6] Devolver Livros")
    print(Fore.RED + "[7] Sair")
    print(Fore.CYAN + Style.BRIGHT + "=" * len(menu_word))


def inserir_menu():
    while True:
        # definir dicionário para cada livro
        livros = dict()

        # input para título de cada livro
        titulo = input("Digite o título do livro: ").strip().lower()

        # Verificação do título na lista biblioteca
        # A função any() retorna um valor bool, neste caso se for True, está registado e fica no loop
        while any(livros['Título'] == titulo for livros in biblioteca):
            print('Esse livro já está registado')
            titulo = input("Digite o título de outro livro: ").strip().lower()
        else:
            livros['Título'] = titulo

        # input para autores
        lista_autores = list()
        while True:
            autor = [input("Digite o autor do livro: ")]
            lista_autores.append(autor)
            continuar = input("O livro tem mais autores?: [S/N] ").strip().lower()
            if continuar == "n":
                break
        livros["Autores"] = lista_autores

        # input para o ISBN
        isbn = input('Digite o ISBN do livro: ')
        while len(isbn) != 13 or isbn.isnumeric() is False:
            isbn = input('Digite correctamente o ISBN do livro: ')
        else:
            livros['ISBN'] = isbn

        # verificação do ISBN na lista biblioteca
        while any(livros['ISBN'] == isbn for livros in biblioteca):
            print('Esse ISBN já está registado...')
            isbn = input("Digite outro ISBN para o livro: ")
        else:
            livros['ISBN'] = isbn

        # input para ano de publicação
        ano_publicacao = (input('Digite o ano de publicação: '))
        while len(ano_publicacao) != 4 or ano_publicacao.isnumeric() is False:
            ano_publicacao = input('Digite correctamente o ano de publicação do livro: ')
        else:
            livros['Ano de publicação'] = ano_publicacao

        # input para editora
        livros['Editora'] = input('Digite a editora do livro: ').strip()

        # input para generos/categorias
        categorias = list()
        while True:
            cat = [input("Digite a categoria do livro: ")]
            categorias.append(cat)
            continuar = input("O livro pode ser identificado com outra categoria?: [S/N] ").strip().lower()
            if continuar == "n":
                livros["Categorias"] = categorias
                break

        # input para a disponibilidade do livro
        status = 'Disponível'
        livros['Status'] = status

        #input para data de requisição
        data_requisicao = ""
        livros['Data de requisição'] = data_requisicao

        #input para pessoa que pediu emprestado
        nome_pessoa = ""
        livros['Pessoa que requisitou'] = nome_pessoa

        # adicionar registo
        biblioteca.append(livros)
        print('Livro registado')

        terminar = input('Deseja registar mais algum livro? [S/N] ').strip().upper()
        if terminar == 'N':
            break


def listar_menu(biblio):
    for livro in biblio:
        for key in livro:
            if livro[key] != "":
                if isinstance(livro[key], list):
                    formated_keys = ', '.join([' '.join(keys) for keys in livro[key]])
                    print(Fore.BLUE + f"{key}: {Fore.WHITE + formated_keys}")
                else:
                    print(Fore.BLUE + f"{key}: {Fore.WHITE + livro[key]}")
        print(Style.RESET_ALL)  # Reset text color/style
        print(Fore.GREEN + "*=*" * 15)
        print()


def remover_livro(ls, op_remover):
    temp_livros = []
    if len(ls) == 0:
        print("Não existe livros na biblioteca")
    else:
        print(f"{op_remover.upper()}S disponiveis: ", end=" ")
        for i, livro in enumerate(ls):
            print(livro[op_remover], end="")
            if i < len(ls) - 1:
                print(", ", end="")
        valor_remover = input(f"\nQual o {op_remover} do livro a remover?: ") if op_remover == "Título" else (
            input(f"\n{op_remover.upper()} do livro a remover: "))

        for livro in ls:
            if livro[op_remover] != valor_remover:
                temp_livros.append(livro)
    return temp_livros


def remover_menu(li):
    global biblioteca
    while True:
        opcao_remover = input("Pretende remover livros a partir do que? [ISBN ou Título]: ").strip()
        while opcao_remover not in ["ISBN", "Título"]:
            print("Opção inválida, escreve ISBN ou Título")
            opcao_remover = input("Pretende remover livros a partir do que? [ISBN ou Título]: ").strip()
        biblioteca = remover_livro(li, opcao_remover)

        opcao_remover = input("Pretende remover mais? [s/n]: ").lower().strip()
        if opcao_remover == "n":
            break
        if len(biblioteca) == 0:
            print("Já não existe livros para remover")
            sleep(1)
            print("A sair do menu de eliminação de livros", end=" ")
            sleep(0.5)
            print(".", end=" ")
            sleep(0.5)
            print(".", end=" ")
            sleep(0.5)
            print(".")
            break

def emprestar(biblio):
    nome_pessoa = input('Qual é o seu nome?: ')
    data_requisicao = str(date.today())
    status = 'Indisponivel'
    for livro in biblio:
        livro['Status'] = status
        livro['Data de requisicao'] = data_requisicao
        livro['Pessoa que requisitou'] = nome_pessoa

def devolver(biblio):
    data_requisicao = ''
    status = 'Disponivel'
    for livro in biblio:
        livro['Status'] = status
        livro['Data de requisicao'] = data_requisicao

biblioteca = [
    {
        'Título': 'ola', 'Autores': [['olad'], ['ola123']], 'ISBN': '1234567890123', 'Ano de publicação': '1321', 'Editora': 'ola',
        'Categorias': [['a']], 'Status': 'Indisponível', 'Data de requisicao': '27/03', 'Pessoa que requisitou': 'Tiago'
    },
    {
        'Título': 'ola123', 'Autores': [['oladddd'], ['ola123444'], ['autorrr']], 'ISBN': '1234567890125', 'Ano de publicação': '3213', 'Editora': 'ola',
        'Categorias': [['a']], 'Status': 'Disponível'
    }
    ]

while True:
    menu_principal()
    choice = input("Escolha um opção (1-7): ").strip()
    if choice == "1":
        inserir_menu()
    elif choice == "2":
        listar_menu(biblioteca)
    elif choice == "3":
        break
    elif choice == "4":
        remover_menu(biblioteca)
    elif choice == "5":
        emprestar(biblioteca)
    elif choice == "6":
        devolver(biblioteca)
    elif choice == "7":
        print("Programa a terminar", end=" ")
        sleep(0.5)
        print(".", end=" ")
        sleep(0.5)
        print(".", end=" ")
        sleep(0.5)
        print(".")
        break
    else:
        print("Escolha inválida. Escolha uma opção entre 1-5.")


