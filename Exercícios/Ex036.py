#Exercicio36
from random import randint


print("======\33[34mJOGO DO PAR OU IMPAR\33[m======")

vitorias = 0

while True:
    print("Escolha a sua opção:")
    print("[1] PAR")
    print("[2] IMPAR")
    opcao = input("Escolha se quer par ou impar [P/I]: ").upper().strip()[0]
    num_utilizador = int(input("Digite o seu número: "))
    num_pc = randint(1, 10)
    soma = num_utilizador + num_pc
    if opcao == "P":
        if soma % 2 == 0:
            print(f"Você ganhou! A sua escolha foi \33[34m{num_utilizador}\33[m, a do pc foi \33[31m{num_pc}\33[m que deu \33[33m{soma}\33[m")
            vitorias += 1
        else:
            print(f"Você perdeu... A sua escolha foi \33[34m{num_utilizador}\33[m, a do pc foi \33[31m{num_pc}\33[m que deu \33[33m{soma}\33[m")
            print(f"A sua winning streak foi de {vitorias} vitorias")
            break
    if opcao == "I":
        if soma % 2 != 0:
            print(f"Você ganhou! A sua escolha foi \33[34m{num_utilizador}\33[m, a do pc foi \33[31m{num_pc}\33[m que deu \33[33m{soma}\33[m")
            vitorias += 1
        else:
            print(f"Você perdeu... A sua escolha foi \33[34m{num_utilizador}\33[m, a do pc foi \33[31m{num_pc}\33[m que deu \33[33m{soma}\33[m")
            print(f"A sua winning streak foi de {vitorias} vitorias")
            break

