#Pedir numero ao utilizador
num_introduzido = int(input("Digite o seu numero: ",))

#Ler opçao de escolha
print("Escolha a base de conversão")
print("[1] - Binário")
print("[2] - Octal")
print("[3] - Hexadecimal")
opcao = int(input("Digite a sua opção: "))

#Mostrar a base de conversao
if opcao == 1:
    print(f"O numero {num_introduzido} em Binário é {bin(num_introduzido)[2:]}")
elif opcao == 2:
    print(f"O numero {num_introduzido} em Octal é {oct(num_introduzido)[2:]}")
elif opcao == 3:
    print(f"O numero {num_introduzido} em Hexadecimal é {hex(num_introduzido)[2:]}")
else:
    print("A sua opção é invalida")
