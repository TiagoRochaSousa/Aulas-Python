#Exercicio29
print("======JOGO DA ADIVINHA======")
print("O computador vai pensar num número aleatório entre 0 a 10 \n")
num_introduzido = int(input("Digite o número que acha que o computador pensou: "))

#importar biblioteca de generar numero aleatorio
import random
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_computador = random.choice(lista)

tentativas = 0

while num_computador != num_introduzido:
    num_introduzido = input("tente novamente:")
    tentativas += 1
    print(num_computador)
else:
    print(f"ACertou e demorou {tentativas} vezes")
