num1 = int(input("Digite o seu primeiro numero: "))
num2 = int(input("Digite o seu segundo numero: "))

if num1 > num2:
    print(f"O seu primeiro numero introduzido {num1} é maior que o segundo {num2}")
elif num2 == num1:
    print("Os seus numeros sao iguais")
else:
    print(f"O seu primeiro numero introduzido {num1} é menor que o segundo {num2}")
