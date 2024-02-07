#pedra,papel,tesoura
print("======PEDRA, PAPEL, TESOURA======")
print("[1] - PEDRA")
print("[2] - PAPEL")
print("[3] - TESOURA")

#escolha do pc
import random
lista = [1, 2, 3]
escolha_pc = random.choice(lista)

#utilizador
opcao = int(input("Escolha a sua opcao: "))

#importar o time
print("Analisando o resultado....")
import time
time.sleep(3)

#calculos
if opcao == escolha_pc:
    print("Empate")
elif opcao == 1 and escolha_pc == 2:
    print("Perdeu, PAPEL GANHA A PEDRA")
elif opcao == 1 and escolha_pc == 3:
    print("Ganhou, PEDRA GANHA A TESOURA")
elif opcao == 2 and escolha_pc == 1:
    print("Ganhou, PAPEL GANHA A PEDRA")
elif opcao == 2 and escolha_pc == 3:
    print("Perdeu, TESOURA GANHA A PAPEL")
elif opcao == 3 and escolha_pc == 1:
    print("Perdeu, PEDRA GANHA A TESOURA")
else:
    print("Ganhou, TESOURA GANHA A PAPEL")

#mostrar escolha do pc
if escolha_pc == 1:
    print("O pc escolheu a opção PEDRA")
elif escolha_pc == 2:
    print("O pc escolheu a opção PAPEL")
else:
    print("O pc escolheu a opção TESOURA")
