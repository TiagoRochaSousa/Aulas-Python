#Exercicio51
from random import randint
numerochaves = int(input("Digite quantas chaves pretende gerar: "))
chave_euromilhoes = list()

for c in range(0, numerochaves):
    chave_numeros = list()
    for n in range(0, 5):
        num = randint(1, 50)
        if num not in chave_numeros:
            chave_numeros.append(num)
        else:
            num = randint(1, 50)
            chave_numeros.append(num)

    chave_estrelas = list()
    for e in range(0, 2):
        num = randint(1, 12)
        if num not in chave_estrelas:
            chave_estrelas.append(num)
        else:
            num = randint(1, 12)
            chave_estrelas.append(num)

    chave_numeros.sort()
    chave_estrelas.sort()

    chave_milhoes = [chave_numeros[:], chave_estrelas[:]]

    chave_euromilhoes.append(chave_milhoes[:])

for i in range(0, numerochaves):
    print(f"As sua chave numero {i +1} do euromilhões é: ")
    print(f"Os seus números são {chave_euromilhoes[i][0]} e as estrelas são {chave_euromilhoes[i][1]}")

