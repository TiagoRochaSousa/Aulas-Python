#Exercicio40
from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

for n in numeros:
    print(n)

print(f"\nO maior numero gerado foi o {max(numeros)}")
print(f"\n O menor número gerado foi o {min(numeros)}")
