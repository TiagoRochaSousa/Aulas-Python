#Exercicio31
num = int(input("Introduza o número pretendido: "))

import math
fatorial = math.factorial(num)
print(f"O fatorial do seu numero introduzido é:{fatorial}")

#outra maneira
print("Maneira mais bonita")
num = int(input("Digite um numero para obter o seu fatorial: "))

c = num

#Iniciar o fatorial
f = 1

while c > 0:
    print(f"{c}", end="")
    print("x" if c > 1 else "=", end="")
    f *= c
    c -= 1
print(f"{f}")
