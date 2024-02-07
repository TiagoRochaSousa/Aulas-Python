#exercicio43

num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))
num_3 = int(input("Digite o terceiro número: "))
num_4 = int(input("Digite o quarto número: "))
num_5 = int(input("Digite o quinto número: "))

lista_um = [num_1, num_2, num_3, num_4, num_5]

max_num = max(lista_um)
min_num = min(lista_um)

print(f"O maior numero inserido é o {max(lista_um)} e está na posição {lista_um.index(max(lista_um))}")
print(f"O menor numero inserido é o {min(lista_um)} e está na posição {lista_um.index(min(lista_um))}")






