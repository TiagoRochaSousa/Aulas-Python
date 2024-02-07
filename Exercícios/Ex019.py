print("======JOGO DA ADIVINHA======")
print("O computador vai pensar num número aleatório entre 0 a 7 \n")
num_introduzido = int(input("Digite o número que acha que o computador pensou: "))

#importar biblioteca de generar numero aleatorio
import random
lista = [0, 1, 2, 3, 4, 5, 6, 7]
num_computador = random.choice(lista)

#Condição
if num_computador == num_introduzido:
    print(f"Parabéns você adivinhou os pensamentos do computador, o número é {num_computador}")
else:
    print(f"A IA é muito forte e escolheu o {num_computador} e tu escolheste o {num_introduzido}")
