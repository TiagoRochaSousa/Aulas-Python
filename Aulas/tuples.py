"""estante = ("playstation", "xbox", "nintendo", "gameboy")

estante_ordem_alfabetica = sorted(estante)
print(estante_ordem_alfabetica)
for consola in estante:
    print(consola)

numeros_extenso =("zero", "um", "dois", "tres", "quatro")
num = int(input("Digite um numero de 0 a 4"))

print(numeros_extenso[num])

print(numeros_extenso.index("dois"))

#listas sao arrays
#nos tuples usamos parenteses curvos nas listas parenteses retos
#listas sao mutaveis, enquanto que as tuples sao imutaveis

o .append acrescenta sempre no final da lista, o insert da para escolher a posicao
para apagar, no remove tem que se meter o elemento, no pop apenas o indice.
estante.remove["nintendo"]
estante.pop(3)
del estante [3]
numeros.sort() -> ordena por ordem crescente
numeros.sort(reverse=True) -> ordena por ordem decrescente


lista = [2, 3, 4, 5]

nova_lista = lista[:] # unica maneira de alterar se for sem o [:] altera nas duas variaveis, "faz uma copia"

nova_lista[0] = 7

print(f"Esta é a lista principal: {lista}")
print(f"Esta é a lista secundaria: {nova_lista}")

for i, v in enumerate(lista):
    print(f"Na posição {i} está o valor {v}")

lista = list()

for cont in range(0, 5):
    num = int(input("Digite um numero: "))
    lista.append(num)
    print(f"O número {num} foi adicionado com sucesso")
for valor in lista:
    print(valor, end=" ")

lista.pop(0)
for valor in lista:
    print("\n", valor, end=" ")"""

