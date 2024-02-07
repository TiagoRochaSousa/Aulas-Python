#Exercicio32
num = int(input("Introduza o seu numero: "))

num1 = 0
num2 = 1

cont = 3

print(f"{num1} ~ {num2}", end="")
while cont <= num:
    num -= 1
    num3 = num1 + num2
    print(f"~ {num3}", end="")
    num1 = num2
    num2 = num3
