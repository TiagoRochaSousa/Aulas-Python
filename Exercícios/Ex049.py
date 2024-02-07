"""#exercicio49

lista = list()

for i in range(0, 3):
    valor = list()
    for v in range(0, 3):
        num = int(input(f"Digite o numero na posição {[i]}{[v]}: "))
        valor.append(num)
    lista.append(valor)


for i in range(0, len(lista)):
    for v in range(0, len(lista[0])):
        print(f"{[lista[i][v]]}", end=" ")
    print()
"""

#outra maneira

matriz = [[[0], [0], [0]], [[0], [0], [0]], [[0], [0], [0]]]

for indice in range(0, 3):
    for valor in range(0, 3):
        matriz[indice][valor] = int(input(f"Digite o valor para [{indice}][{valor}]: "))

for indice in range(0, 3):
    for valor in range(0, 3):
        print(f"[ {matriz[indice][valor]} ]", end=" ")
    print()
