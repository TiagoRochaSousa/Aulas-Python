"""num = 7

for c in range(0,10):
    print(num, "x", c+1, "=", num * (c + 1))"""

"""i = 1
f = 10
salto = 2

for michaelJordan in range(i, f, salto):
    print(michaelJordan)"""

"""tentativas = 0
mensagem = "Bem Vindo"
password = "Dr.House"

for c in range(0, 3):
    entrada = input("Insira a password: ")
    if entrada == password:
        print(mensagem)
    else:
        tentativas = tentativas + 1
        print("Tente novamente...\n")

    if tentativas == 3:
        print("utilizador bloqueado")"""

"""#Exercicio 21
import time

#Loop
for c in range(0, 10):
    print(10 - c)
    time.sleep(1)

print("fogooooooo")"""

"""#""Exercicio 22, numeros pares entre 1 a 100
for c in range(1, 101, 2):
    print(c+1)"""

"""#OU
for c in range(0, 100):
    if c == 0:
        continue
    elif c % 2 == 0:
        print(c)"""

"""#Exercicio23
num = int(input("Introduza um numero inteiro: "))

for c in range(0, 10):
    tabuada = num * (c + 1)
    print(num, "x", c+1, "=", tabuada)"""

"""#Exercicio24 programa que leio se o numero é primo
num = int(input("Introduza um numero inteiro: "))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        tot += 1                  #igual a tot=tot +1

if tot == 2:
    print(f"O número {num} é primo, foi divisivel {tot} vezes")
else:
    print(f"O número {num} não é primo, foi divisil {tot} vezes")"""

"""#Exercicio25 - executar uma frase para indicar se é um palindromo
frase = input("Introduza uma frase: ").strip().upper()
palavras = frase.split()
juntas = "".join(palavras)
inverso = juntas[::-1]
tam = len(juntas)

for c in range(0, tam):
    if juntas[c] != inverso[c]:
        print("Não é um palindromo")
        break
    if c == tam - 1:
        print("é um palindromo")


print(juntas)
print(inverso)"""

"""#Exercicio26
#imports
from datetime import date
ano_atual = date.today().year

#Variaveis de controlo
maiores_idade = 0
menores_idade = 0

#Rodar for para leitura e analise de idades
for c in range(1, 8):
    ano_nascimento = int(input(f"Digite o ano em que a {c} pessoa nasceu: "))
    if ano_atual - ano_nascimento < 18:
        menores_idade += 1
        print("A pessoa é menor de idade")
    else:
        maiores_idade += 1
        print("A pessoa á maior de idade")

#Exibir no ecra os dados
print(f"Existem {menores_idade} pessoas menores de idade e {maiores_idade} maiores de idade")"""

"""#Exercicio27

#variaveis de controlo
maior_idade = 0
menor_idade = 0

for pessoa in range(1, 11):
    idade = int(input(f"Digite a idade da pessoa {pessoa}: "))
    if pessoa == 1:
        maior_idade = idade
        menor_idade = idade
    else:
        if idade > maior_idade:
            maior_idade = idade
        elif idade < menor_idade:
            menor_idade = idade

print(f"maior idade {maior_idade}, menor idade {menor_idade}")"""

"""#Exercicio28
resposta = ""

while resposta != "V" or "F":
    print("A terra é plana?")
    resposta = input("---> ").upper()
    if resposta == "V":
        print("A resposta está errada")
        break
    elif resposta == "F":
        print("A resposta está certa")
        break
    else:
        print("A sua resposta nao esta bem formatada digite novamente:")
while resposta != "V" or "F":
    print("A lua gira em torno da Terra?")
    resposta = input("---> ").upper()
    if resposta == "V":
        print("A resposta está certa")
        break
    elif resposta == "F":
        print("A resposta está errada")
        break
    else:
        print("A sua resposta nao esta bem formatada digite novamente:")
while resposta != "V" or "F":
    print("A Terra gira em torno do Sol?")
    resposta = input("---> ").upper()
    if resposta == "V":
        print("A resposta está certa")
        break
    elif resposta == "F":
        print("A resposta está errada")
        break
    else:
        print("A sua resposta nao esta bem formatada digite novamente:")"""

"""#Exercicio29
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
    print(f"ACertou e demorou {tentativas} vezes")"""


