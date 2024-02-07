#Exercicio30
#variavel
resposta = 0

num1 = int(input("introduza o primeiro numero: "))
num2 = int(input("introduza o segundo numero: "))
num3 = int(input("introduza o terceiro numero: "))


while resposta != 5:
    print("Escolha uma das seguintes opções: \n")
    print(" [1] SOMAR")
    print(" [2] MULTIPLICAR")
    print(" [3] MAIOR")
    print(" [4] NOVOS NÚMEROS")
    print(" [5] SAIR DO PROGRAMA")

    resposta = int(input("Qual a sua opção: "))
    if resposta == 1:
        soma = num1 + num2 + num3
        print(f"A soma dos seus números é: {soma}")
    elif resposta == 2:
        multiplicacao = num1 * num2 * num3
        print(f"A multiplicação dos seus números é: {num1} * {num2} * {num3} = {multiplicacao}")
    elif resposta == 3:
        maior = num1
        if num2 > maior and num2 > num3:
            maior = num2
        elif num3 > maior and num3 > num2:
            maior = num3
        print(f"O maior número introduzido é {maior}")
    elif resposta == 4:
        print("Escolha novos numeros: ")
        num1 = int(input("introduza o primeiro numero: "))
        num2 = int(input("introduza o segundo numero: "))
        num3 = int(input("introduza o terceiro numero: "))
else:
    print("Saiu do programa!")
