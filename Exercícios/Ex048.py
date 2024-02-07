#Exercicio48
lista = list()
lista_par = list()
lista_impar = list()

for v in range(0, 10):
    valor = int(input("Digite o seu número: "))
    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)

lista.append(lista_par)
lista.append(lista_impar)

print(lista)
print(f"A lista de numeros pares é {sorted(lista[0])}")
print(f"A lista de numeros ímpares é {sorted(lista[1])}")

"""#Outra maneira
lista = [[], []]

for cont in range(0, 10):
    num = int(input(f"Digite o {cont + 1} número: "))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)"""
