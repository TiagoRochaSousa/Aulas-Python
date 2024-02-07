matriz = list()

for i in range(0, 3):
    valor = list()
    for v in range(0, 3):
        num = int(input(f"Digite o número na posição {[i]}{[v]}: "))
        valor.append(num)
    matriz.append(valor)

# Exibindo a matriz
for i in range(0, len(matriz)):
    for v in range(0, len(matriz[i])):
        print(f"{matriz[i][v]}", end=" ")
    print()
