#Exercicio41

a = int(input("Introduza um numero de 0 a 9: "))
b = int(input("Introduza um numero de 0 a 9: "))
c = int(input("Introduza um numero de 0 a 9: "))
d = int(input("Introduza um numero de 0 a 9: "))

numeros = (a, b, c, d)

countsete = 0
pares = 0
posicao = 0

for n in numeros:
    print(n)
    if n == 7:
        countsete += 1
    elif n % 2 == 0:
        pares += 1

print(f"O numero 7 aparece {countsete} vezes")
print(f"existem {pares} numeros pares")

print(f"O numero 5 esta na posicao {numeros.index(5) + 1}")

