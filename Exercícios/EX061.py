#Exercicio61
from time import sleep

def conta_numeros(*num):
    resposta = 0
    maior = 0
    while True:
        num = int(input("Digite o numero: "))
        resposta = input("Deseja continuar? [S/N]: ").upper().strip()
        if num == 0:
            maior = num
        else:
            if num > maior:
                maior = num
        if resposta == "N":
            break
    print(f"O maior numero que inseriu foi o {maior}")

conta_numeros()
