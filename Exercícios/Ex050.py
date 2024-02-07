#Exercicio50

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for indice in range(0, 3):
    for valor in range(0, 3):
        matriz[indice][valor] = int(input(f"Digite o valor para [{indice}][{valor}]: "))

for indice in range(0, 3):
    for valor in range(0, 3):
        print(f"[ {matriz[indice][valor]} ]", end=" ")
    print()

soma = 0

for indice in range(0, 3):
    for valor in range(0, 3):
        if matriz[indice][valor] % 2 == 0:
            soma += matriz[indice][valor]
print(f"A soma de todos os valores pares é {soma}")

#soma valores segunda coluna

soma2coluna = 0

for indice in range(0, 3):
    for valor in range(1):
        soma2coluna += matriz[indice][1]
print(soma2coluna)

#maior valor 3 linha

maior = 0

for indice in range(0, 3):
    for valor in range(0, 3):
        if maior == 0:
            maior = matriz[2][valor]
        elif matriz[2][valor] > maior:
            maior = matriz[2][valor]
print(f"O maior numero da terceira coluna é o {maior}")




