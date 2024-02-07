#Exercicio33
cont = 0
opt = ""
soma = 0

while True:
    num = int(input("Digite o numero: "))
    soma += num
    cont += 1
    opt = input("Quer continuar? [S/N]: ").upper().strip()[0]
    if opt in "Nn":
            break
print(f"Digitou {cont} numeros e a soma dos mesmos é {soma}")
